import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

fPath = "C:/Users/win7/Desktop/"
fName = "top500JobAllUserLog_201604_part.csv"
data = pd.read_csv(fPath + fName, delimiter = "|")


def job_bind_uid():
    job_apply = data.loc[(data['action']=='viewJob')]
    job_apply_group = job_apply.groupby('jobNo').size()
    job_apply_group = pd.DataFrame(job_apply_group,columns=['count'])
    
    job_uid_bind={}
    for i in job_apply_group.index[::]:
        job_uid_bind[i]=[]
        
    for i in job_apply_group.index[::]:
        for j in job_apply['uid'].loc[(job_apply['jobNo'] == i)]:
            if(j not in job_uid_bind[i]):
                job_uid_bind.setdefault(i,[]).append(j)
    return job_uid_bind


def uid_bind_job():
    job_apply = data.loc[(data['action']=='applyJob')]
    uid_apply_group = job_apply.groupby('uid').size()
    uid_apply_group = pd.DataFrame(uid_apply_group,columns=['count'])
      
    uid_bind_job={}
    for i in uid_apply_group.index[::]:
        uid_bind_job[i]=[]
        
    for i in uid_apply_group.index[::]:
        for j in job_apply['jobNo'].loc[(job_apply['uid'] == i)]:
            if(j not in uid_bind_job[i]):
                uid_bind_job.setdefault(i,[]).append(j)
    return uid_bind_job


def job_pred(job_bind_uid , uid_bind_job):  
    
    job_apply = data.loc[(data['action']=='viewJob')]
    uid_view_group = job_apply.groupby('jobNo').size()


    job_pred = {}    
    for i in uid_view_group.index[::]:
        job_pred[i]=[]

    for t in uid_view_group.index[::]:
        for i in job_bind_uid[t]:
            if(i in uid_bind_job):
                for j in uid_bind_job[i]:
                    if(j not in job_pred[t]):
                        job_pred.setdefault(t,[]).append(j)
    
    for i in uid_view_group.index[::]:
        if(job_pred[i]==[] or job_pred[i]==[i]):
            del job_pred[i]
   
    return job_pred
    
job_bind_uid = job_bind_uid()    
uid_bind_job = uid_bind_job()
job_pred = job_pred(job_bind_uid , uid_bind_job)


#row = PrettyTable()
#row.field_names = ["有看沒應徵", "應徵其他工作"]

#for i in job_pred.keys():
#    if(int(len(job_pred[i])<=3)):
#       row.add_row([i,job_pred[i]])   
#print (row)







