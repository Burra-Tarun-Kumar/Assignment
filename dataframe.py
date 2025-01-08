import pandas as pd
screen_time=[2,4,6,7,1]
study_hours=[9,7,3,6,8]
stu_name=["Tarun","Aryan","Chandu","BVR","rohith"]
dict1={
    'screen_time':screen_time,
    'study_hours':study_hours,
    'stu_name':stu_name
}
df=pd.DataFrame(dict1)
print(df)
