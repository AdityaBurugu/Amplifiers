from Other_Func import format_value
from CE_AMP import CE_Amplifier
from CC_AMP import CC_Amplifier
from RF_D import Resonating_Freq_Design


def CE():
    print("Parameters of CE Amplifier")
    Vcc = float(input("Enter Vcc Value:"))
    Vce = float(input("Enter VceQ Value:"))
    if Vce > Vcc:
        print("Vce is greater than VCC")
        exit(0)
    IcQ = input("Enter IcQ Value:")
    B = int(input("Enter Beta Value:"))
    Av = int(input("Enter required Gain:"))
    Rc, Re, R1, R2 = CE_Amplifier(Vcc, Vce, IcQ, B, Av)
    print("Emitter Resistance:", Re, "ohm")
    print("Collector Resistance:", Rc, "ohm")
    print("Biasing Resistance1:", R1, "ohm")
    print("Biasing Resistance2:", R2, "ohm")

def CC():
    print("Parameters of CC Amplifier")
    Vcc = float(input("Enter Vcc Value:"))
    Vce = float(input("Enter VceQ Value:"))
    if Vce > Vcc:
        print("Vce is greater than VCC")
        exit(0)
    IcQ = input("Enter IcQ Value:")
    B = int(input("Enter Beta Value:"))
    Rin,Re, R1, R2 = CC_Amplifier(Vcc, Vce, IcQ, B)
    print("Impedence Matching Resistance:", Rin, "ohm")
    print("Emitter Resistance:", Re, "ohm")
    print("Biasing Resistance1:", R1, "ohm")
    print("Biasing Resistance2:", R2, "ohm")

def Freq():
    R = input("Enter Resistance Value:")
    C = input("Enter Capacitance Value:")
    print("Resonating Frequency:",format_value(Resonating_Freq_Design(R,C)))


def main():
    print("Select Amplifier\n1.CE Amplifier\n2.CC Amplifier\n3.Resonating Freq of RC Circuit")
    choice = int(input("Enter your choice:"))
    if choice==1:
        CE()
    elif choice==2:
        CC()
    elif choice==3:
        Freq()
    else:
        print("Invalid Choice")

if __name__ == '__main__':
    main()