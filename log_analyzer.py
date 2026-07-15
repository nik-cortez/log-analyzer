import sys
import datetime as dt

def main():
    filename = input("File: ")
    logs = read_file(filename)
    alerts = count_logs(logs)
    display_results(alerts)
    print("Report generated succesfully")

def read_file(file):
    try: 
        with open (file, "r") as logs: 
            return logs.readlines()
    
    except FileNotFoundError:
        sys.exit("File not found")
        
def count_logs(logs):
    alert = {
    }

    for log in logs:
        log = log.strip()
        
        if not log:
            continue

        date, time, alerts, *msg = log.split()

        if alerts in alert:
            alert[alerts] += 1
        else:
            alert[alerts] = 1
    
    return alert
    
def display_results(alert):
    sorted_alert = sorted(alert.items(), key=lambda x:x[1], reverse=True)
    
    today = dt.date.today()

    with open ("report.txt", "w") as file:
        file.write(f"Report Generated: {today} \n\n")

        for k, v in sorted_alert:
            file.write(f"{k}: {v}\n")


if __name__ == "__main__":
    main()