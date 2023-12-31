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
    re = (26*10**-3)/(Ic)
    Rc = round(Av*re,2)

    Re = (VCC-Ic*Rc-Vce)/(Ic)

    Vdrop_across_Re = Ic*Re
    VBE = 0.7       #fixed
    Base_Voltage = (Vdrop_across_Re+VBE)


    ratio = ((VCC-Base_Voltage)/Base_Voltage)

    R2_max = B/10*Re

    R2 = int(input(f'''Select R2 Value less than {format_value(R2_max)}Ω:'''))
    if R2>0 and R2<=R2_max:
        R1 = ratio*R2

        Rc = format_value(Rc)
        Re = format_value(Re)
        R1 = format_value(R1)
        R2 = format_value(R2)

        return Rc,Re,R1,R2
    else:
        return None,None,None,None

def CC_Amplifier(VCC,Vce,Ic,B):

    Re = Vce/Ic
    VBE = 0.7  # fixed
    Base_Voltage = (Vce + VBE)

    ratio = round((VCC-Base_Voltage)/Base_Voltage,1)

    R2_max = B/10*Re

    R2 = int(input(f'''Select R2 Value less than {format_value(R2_max)}Ω:'''))
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

def CE_RC_Coupled_Amplifier():
    pass
def CE():
    Vcc = float(input("Enter Vcc Value:"))
    Vce = float(input("Enter VceQ Value:"))
    if Vce > Vcc:
        print("Vce is greater than VCC")
        exit(0)
    IcQ = float(input("Enter IcQ Value:"))
    B = int(input("Enter Beta Value:"))
    Av = int(input("Enter required Gain:"))
    Rc, Re, R1, R2 = CE_Amplifier(Vcc, Vce, IcQ, B, Av)
    print("Emitter Resistance:", Re, "ohm")
    print("Collector Resistance:", Rc, "ohm")
    print("Biasing Resistance1:", R1, "ohm")
    print("Biasing Resistance2:", R2, "ohm")

def CC():
    Vcc = float(input("Enter Vcc Value:"))
    Vce = float(input("Enter VceQ Value:"))
    if Vce > Vcc:
        print("Vce is greater than VCC")
        exit(0)
    IcQ = float(input("Enter IcQ Value:"))
    B = int(input("Enter Beta Value:"))
    Rin,Re, R1, R2 = CC_Amplifier(Vcc, Vce, IcQ, B)
    print("Impedence Matching Resistance:", Rin, "ohm")
    print("Emitter Resistance:", Re, "ohm")
    print("Biasing Resistance1:", R1, "ohm")
    print("Biasing Resistance2:", R2, "ohm")

def main():
    print("Select Amplifier\n1.CE Amplifier\n2.CC Amplifier")
    choice = int(input("Enter your choice:"))
    if choice==1:
        CE()
    elif choice==2:
        CC()
    else:
        print("Invalid Choice")

if __name__ == '__main__':
    main()