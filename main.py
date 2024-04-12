import numpy as np

def format_value(value):
    if abs(value) >= 1e6:
        formatted_value = round(value / 1e6,2)
        unit = 'M'
    elif abs(value) >= 1e3:
        formatted_value = round(value / 1e3,2)
        unit = 'k'
    else:
        formatted_value = round(value,2)
        unit = ''

    return f"{formatted_value}{unit}"

def CE_Amplifier(VCC,Vce,Ic,B,Av):
    Ic=eval(Ic)
    re = (26*10**-3)/(Ic)
    Rc = round(Av*re,2)

    Re = (VCC-Ic*Rc-Vce)/(Ic)

    Vdrop_across_Re = Ic*Re
    VBE = 0.7       #fixed
    Base_Voltage = (Vdrop_across_Re+VBE)


    ratio = ((VCC-Base_Voltage)/Base_Voltage)

    R2_max = B/10*Re

    R2 = eval(input(f'''Select R2 Value less than {format_value(R2_max)}Ω:'''))
    if R2>0 and R2<=round(R2_max):
        R1 = ratio*R2

        Rc = format_value(Rc)
        Re = format_value(Re)
        R1 = format_value(R1)
        R2 = format_value(R2)

        return Rc,Re,R1,R2
    else:
        return None,None,None,None

def CC_Amplifier(VCC,Vce,Ic,B):
    Ic=eval(Ic)
    Re = Vce/Ic
    VBE = 0.7  # fixed
    Base_Voltage = (Vce + VBE)

    ratio = round((VCC-Base_Voltage)/Base_Voltage,1)

    R2_max = B/10*Re

    R2 = eval(input(f'''Select R2 Value less than {format_value(R2_max)}Ω:'''))
    if R2>0 and R2<=R2_max:
        R1 = ratio*R2
        Rin = (R1 * R2) / (R1 + R2)
        Re = format_value(Re)
        R1 = format_value(R1)
        R2 = format_value(R2)
        Rin = format_value(Rin)

        return Rin,Re,R1,R2
    else:
        return None,None,None,None

def LP_HP_RC(R,C):
    f=1/(2*np.pi*eval(R)*eval(C))
    return f

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
    print("Resonating Frequency:",format_value(LP_HP_RC(R,C)))


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