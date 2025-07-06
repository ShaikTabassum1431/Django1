import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle 
df=pd.read_csv("C:\\Users\\mansu\\OneDrive\\Desktop\\internpurple\\day2ml\\diabetes.csv")
df.isnull().sum()
df=df.drop_duplicates()
df['Pregnancies']=df['Pregnancies'].replace(0,df['Pregnancies'].mean())
df['Glucose']=df['Glucose'].replace(0,df['Glucose'].mean())
df['BloodPressure']=df['BloodPressure'].replace(0,df['BloodPressure'].mean())
df['SkinThickness']=df['SkinThickness'].replace(0,df['SkinThickness'].mean())
df['Insulin']=df['Insulin'].replace(0,df['Insulin'].mean())
x=df.drop(columns='Outcome',axis=1)
y=df['Outcome']
sc=StandardScaler() #numbers to binary 
x=sc.fit_transform(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
 # type: ignore
model1=RandomForestClassifier()
model1.fit(x_train,y_train)
y_pred1=model1.predict(x_test)
res1=accuracy_score(y_test,y_pred1)
print(res1)
filename='diabetics.pkl' 
pickle.dump(model1,open(filename,'wb')) 
"""
l=[] 
p=int(input("Enter no.of pregnancies:")) 
g=int(input("Glucose")) 
B=int(input("Bloodpressure"))
s=int(input("skinthickness")) 
i=int(input("insulin"))
b=float(input("bmi")) 
d=float(input("diabeties")) 
a=int(input("age")) 
l.append([p,g,B,s,i,b,d,a]) 
l=sc.fit_transform(l) 
ans=load_model.predict(l) 
if ans[0]==0:
    print("NO") 
else:
    print("YES")"""


