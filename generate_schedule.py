from scheduler import ShiftScheduler
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_schedule.py YEAR MONTH")
        return
    
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    
    scheduler = ShiftScheduler()
    schedule = scheduler.generate_schedule(year, month)
    
    # Save to files
    filename = f"{datetime(year, month, 1).strftime('%B_%Y')}"
    schedule.to_csv(f"output/{filename}.csv")
    schedule.to_excel(f"output/{filename}.xlsx")
    
    print(f"Schedule generated for {filename}")

if __name__ == "__main__":
    main()
