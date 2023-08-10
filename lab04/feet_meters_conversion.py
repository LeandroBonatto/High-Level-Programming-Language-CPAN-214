def foot_to_meter(foot):
    meter = foot / 3.28084
    return meter

def meter_to_foot(meter):
    foot = meter * 3.28084
    return foot

print("Feet     Meter")

for foot in range(1, 11):
    meter = foot_to_meter(foot)
    print(" {:.1f}     {:.2f}".format(foot, meter))

print(" ***************")
print(" Meter    Feet")
for meter in range(20, 75, 6):
    foot = meter_to_foot(meter)
    print(" {:.1f}     {:.2f}".format(meter, foot))


