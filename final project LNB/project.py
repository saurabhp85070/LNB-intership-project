import pickle
import pandas as pd
from pip import main


def menu():
    print("---------------------------------------------------")
    print("*****MENU BAR*****")
    print("[1] Profit prediction")
    print("[2] Heart disease prediction")
    print("[3] Diabetes prediction")
    print("[4] Flower species prediction")
    print("[5] Breast cancer prediction")
    print("[6] Wine quality prediction")
    print("[7] Bike reantal prediction")
    print("[8] Medical cost prediction")
    print("[9] Mobile price classification")
    print("[0]  EXIT")
    print("---------------------------------------------------")

    choice=int(input("\nEnter your Choice : "))
    while(check(choice)):
        if(choice==1):
            profit()
        elif(choice==2):
            heart()
        elif(choice==3):
            diabetes()
        elif(choice==4):
            flower()
        elif(choice==5):
            cancer()
        elif(choice==6):
            wine()
        elif(choice==7):
            bike()
        elif(choice==8):
            medical()
        elif(choice==9):
            mobile()
        elif(choice==0):
            print("\nAPPLICATION CLOSED")
            print("\n****THANK YOU FOR YOUR VISIT****\n")
            exit()

# checking for valid choice choosed by user
def check(choice):
    if(choice >= 0 and choice <= 9):
        return True
    else:
        print("\n******INVALID CHOICE******\n")
        return False



# below will load all saved model one by one as per asked by user
# ask for required input paramter for maikg prediction

#================PROFIT PREDICTION===========================================
def profit():
    spend1=float(input("Enter R&D spend : "))
    admr=float(input("Enter Administration : "))
    spend2=float(input("Enter Marketing Spend : "))
    print("press[0] for California, press[1] for Florida, press[2] for New York")
    state=int(input("Enter State : "))
    test=[[spend1,admr,spend2,state]]

    with open("./SavedModels/model1","rb") as f:
        lr=pickle.load(f)
    value=lr.predict(test)
    print("Prediction: ",value)
    menu()
#===============================================================================

#=============================HEART DISEASE PREDICTION============================
def heart():
    age=int(input("Enter Age: "))

    print("press[1] for Male, press[0] for Female")
    sex=int(input("Enter sex: "))

    print("[1] for typical angina,[2] for atypical angina,[3] for non-anginal pain,[4] for asymptomatic")
    cp=int(input("Enter chest pain type: "))

    trtbps=int(input("Enter resting blood pressure (in mm Hg): "))

    chol=int(input("Enter cholestoral in mg/dl fetched via BMI sensor: "))

    fbs=int(input("Enter (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false): "))

    print("[0] for normal,[1] for having ST-T wave abnormality,[2] for showing probable")
    restecg=int(input("Enter resting electrocardiographic results: "))

    thalachh=int(input("Enter maximum heart rate achieved: "))

    exng=int(input("Enter exercise induced angina (1 = yes; 0 = no): "))

    oldpeak=float(input("Enter oldpeak: "))
    slp=int(input("Enter slp: "))

    caa=int(input("Enter number of major vessels (0-3): "))

    thall=int(input("Enter thall: "))

    lst=[[age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]]
    with open("./SavedModels/model2","rb") as f:
        lr=pickle.load(f)
    value=lr.predict(lst)
    if value==1:
        print("More chance of heart attack")
    else:
        print("less chance of heart attack")
    menu()
#====================================================================================

#=======================DIABETES PREDICTION=============================================
def diabetes():
    Pregnancies=int(input("Enter No. of Pregnancies: "))
    Glucose=int(input("Enter Glucose: "))
    BloodPressure=int(input("Enter Blood Pressure: "))
    SkinThickness=int(input("Enter Skin Thickness: "))
    Insulin=int(input("Enter Insulin: "))
    BMI=float(input("Enter BMI: "))
    DiabetesPedigreeFunction=float(input("Enter DiabetesPedigreeFunction: "))
    Age=int(input("Enter age: "))
    lst=[[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]

    with open("./SavedModels/model3","rb") as f:
        lr=pickle.load(f)
    value=lr.predict(lst)
    if value==1:
        print("Prediction: Yes")
    else:
        print("Prediction: No")
    menu()
#=====================================================================================

#======================FLOWER SPECIES PREDICTION=========================================
def flower():
    sepal_length=float(input("Enter sepal length: "))
    sepal_width=float(input("Enter sepal width: "))
    petal_length=float(input("Enter petal length: "))
    petal_width=float(input("Enter sepal width: "))
    lst=[[sepal_length,sepal_width,petal_length,petal_width]]
    with open("./SavedModels/model4","rb") as f:
        lr=pickle.load(f)
    value=lr.predict(lst)
    print("Prediction: ",value)
    menu()
#================================================================================

#=======================BREAST CANCER PREDICTION======================================
def cancer():
    mr=float(input("Enter mean radius: "))
    mt=float(input("Enter mean texture: "))
    mp=float(input("Enter mean perimeter: "))
    ma=float(input("Enter mean area: "))
    ms=float(input("Enter mean smoothness: "))
    
    lst=[[mr,mt,mp,ma,ms]]
    with open("./SavedModels/model5","rb") as f:
        lr=pickle.load(f)
    value=lr.predict(lst)
    if value==1:
        print("Prediction: Yes")
    else:
        print("Prediction: No")
    menu()
#========================================================================================

#==========================WINE QUALITY PREDICTION=========================================
def wine():
    fa=float(input("Enter fixed acidity: "))
    va=float(input("Enter volatile acidity: "))
    ca=float(input("Enter citric acid: "))
    rs=float(input("Enter residual sugar: "))
    cl=float(input("Enter chlorides: "))
    fsd=float(input("Enter free sulfur dioxide: "))
    # tsd=float(input("Enter total sulfur dioxide: "))
    den=float(input("Enter density: "))
    ph=float(input("Enter pH: "))
    sulp=float(input("Enter sulphates: "))
    ol=float(input("Enter alcohol: "))
    wt=int(input("Enter wine type(Red=0,White=1): "))
    lst=[[fa,va,ca,rs,cl,fsd,den,ph,sulp,ol,wt]]

    with open("./SavedModels/model6","rb") as f:
        lr=pickle.load(f)
    value=lr.predict(lst)
    if value==1:
        print("Prediction: Good")
    else:
        print("Prediction: Bad")
    menu()
#===============================================================================================

#===================BIKE RENTAL PREDICTION==================================================
def bike():
    season=int(input("Enter Season ( 1 = spring, 2 = summer, 3 = fall, 4 = winter ): "))
    hldy=int(input("Enter holiday( 1 = Yes , 0 = No ): "))
    wrkdy=int(input("Enter workingday( 1 = Yes , 0 = No ): "))
    print("""\n1: Clear, Few clouds, Partly cloudy, Partly cloudy\n 
                2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist\n
                    3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds\n
                        4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog \n""")
    wthr=int(input("Enter weather( 1 2 3 4): "))
    temp=float(input("Enter temperature in Celsius: "))
    atemp=float(input("Enter 'feels like' temperature in Celsius: "))
    humd=int(input("Enter relative humidity: "))
    wndspd=float(input("Enter wind speed: "))
    dow=int(input("Enter day of week: "))
    hr=int(input("Enter Hour: "))
    mon=int(input("Enter Month(MM): "))
    yr=int(input("Enter year(YYYY): "))
    lst=[[season,hldy,wrkdy,wthr,temp,atemp,humd,wndspd,dow,hr,mon,yr]]

    with open("./SavedModels/model7","rb") as f:
        lr=pickle.load(f)
    value=lr.predict(lst)
    print("prediction: ",value)
    menu()
#=======================================================================================

#==============MEDICAL INSURANCE PREDICTION===========================================
def medical():
    age=int(input("Enter Age: "))
    sex=int(input("Enter sex(Male = 1, Female = 0): "))
    bmi=int(input("Enter BMI: "))
    child=int(input("Enter no. of child: "))
    smoker=int(input("Press [1] if you smoke, else Press [0]: "))
    reg=int(input("Enter region(South-west=3, South-east=2, North-west=1, North-east=0): "))
    lst=[[age,sex,bmi,child,smoker,reg]]

    with open("./SavedModels/model8","rb") as f:
        lr=pickle.load(f)
    value=lr.predict(lst)
    print("Prediction: ",value)
    menu()
#================================================================================================

#================MOBILE PRICE CLASSIFICATION==============================================
def mobile():
    bp=int(input("Enter Battery power: "))
    blue=int(input("Bluetooth (1=YES 0=NO): "))
    clk=float(input("Enter clock speed: "))
    sim=int(input("dual sim (1=YES 0=NO): "))
    fc=int(input("Front Camera mega pixels: "))
    fg=int(input("Has 4G or not (1=YES 0=NO): "))
    imem=int(input("Internal Memory(in GB): "))
    mdep=float(input("Mobile Depth in cm: "))
    wt=float(input("Weight of mobile phone: "))
    nc=int(input("Number of cores of processor: "))
    pc=int(input("Primary Camera mega pixels: "))
    pxht=float(input("Pixel Resolution Height: "))
    pxwd=float(input("Pixel Resolution Width: "))
    ram=int(input("RAM (in GB): "))
    sch=float(input("Screen Height of mobile in cm: "))
    scw=float(input("Screen Width of mobile in cm: "))
    tlkt=float(input("longest time that a single battery charge will last: "))
    tg=int(input("Has 3G or not (1=YES 0=NO): "))
    tch=int(input("Has touch screen or not (1=YES 0=NO): "))
    wifi=int(input("Has wifi or not (1=YES 0=NO): "))
    lst=[[bp,blue,clk,sim,fc,fg,imem,mdep,wt,nc,pc,pxht,pxwd,ram,sch,scw,tlkt,tg,tch,wifi]]

    with open("./SavedModels/model9","rb") as f:
        lr=pickle.load(f)
    value=lr.predict(lst)
    print("Prediction: ",value)
    menu()
#======================================================================================

#===========END============END==============END=================END=================END
if __name__ == "__main__":
    menu()

#==================THANK YOU============================================================


