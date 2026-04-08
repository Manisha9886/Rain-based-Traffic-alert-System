df = pd.read_excel("rain_traffic_dataset.xlsx")

print("Dataset Loaded!\n")

print(" CLASS DISTRIBUTION:\n")
class_counts = df['Risk'].value_counts()

print(class_counts)

#sending Dummy Alerts
def send_bulk_alert(class_counts):
    print("\n ALERT SYSTEM ")

    for risk, count in class_counts.items():
        if risk in ["High", "Critical"]:   # send alerts only for dangerous
            print(f"\n {count} HIGH RISK CASES DETECTED")
            print(" Sending alert to nearby patrol units...")
            print(" Location: Bangalore Zone")
            print(" Patrol Notified: Patrol Unit A\n")
        else:
            print(f"\n {risk} cases are normal ({count} entries)")

send_bulk_alert(class_counts)
