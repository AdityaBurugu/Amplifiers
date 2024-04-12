from Other_Func import format_value
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