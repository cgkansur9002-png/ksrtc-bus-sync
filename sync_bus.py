from supabase import create_client, Client

# 1. Setup - USE YOUR ACTUAL VALUES HERE
import os
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, secret_key)

# 2. Data from your KSRTC screenshot
    # UPDATE: I have added 'seats_left' for all 10 buses from your screenshot
bus_list = [
    {"service_no": "2031BNGGKN", "bus_type": "PALLAKKI (NON AC SLEEPER)", "departure": "20:31", "arrival": "04:30", "seats_left": "11 Seats"},
    {"service_no": "2120BNGSRS", "bus_type": "NON AC SLEEPER", "departure": "21:20", "arrival": "07:40", "seats_left": "16 Seats"},
    {"service_no": "2150BNGSRS", "bus_type": "NON AC SLEEPER", "departure": "21:50", "arrival": "07:20", "seats_left": "16 Seats"},
    {"service_no": "2206BNGSRS", "bus_type": "NON AC SLEEPER", "departure": "22:06", "arrival": "07:00", "seats_left": "24 Seats"},
    {"service_no": "2229BNGSRS", "bus_type": "NON AC SLEEPER", "departure": "22:29", "arrival": "07:30", "seats_left": "17 Seats"},
    {"service_no": "2002BNGDND", "bus_type": "KARNATAKA SARIGE", "departure": "20:02", "arrival": "06:02", "seats_left": "29 Seats"},
    {"service_no": "2035BNGGKN", "bus_type": "KARNATAKA SARIGE", "departure": "20:35", "arrival": "06:15", "seats_left": "28 Seats"},
    {"service_no": "2122BNGSRS", "bus_type": "KARNATAKA SARIGE", "departure": "21:22", "arrival": "06:00", "seats_left": "25 Seats"},
    {"service_no": "2145BNGSRS", "bus_type": "KARNATAKA SARIGE", "departure": "21:45", "arrival": "06:30", "seats_left": "39 Seats"},
    {"service_no": "1600TPTKMT", "bus_type": "KARNATAKA SARIGE", "departure": "23:00", "arrival": "08:45", "seats_left": "39 Seats"}
]

# 3. Push to 'bus_schedule' table
try:
    print("Syncing data to backhand...")
    # This uses 'upsert' so it updates existing buses instead of duplicating them
    response = supabase.table("bus_schedule").upsert(bus_list).execute()
    print("SUCCESS! Check your Supabase Table Editor.")
except Exception as e:
    print(f"Error: {e}")
