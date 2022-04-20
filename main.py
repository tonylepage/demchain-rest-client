import subprocess
import time
import json
from subprocess import TimeoutExpired
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Measurement(BaseModel):
    location: str
    cdn: str
    measuredepoch: Optional[int] = None
    rtt: int
    provider: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/measurements")
def getAllMeasurements():
    result = subprocess.Popen(["docker", "exec", "-t",  "cli",
        "peer", "chaincode", "invoke" ,"--tls", "--cafile", "/opt/home/managedblockchain-tls-chain.pem", "--channelID", "demchannel" ,"--name" ,"demcc" ,"-c",
        '{"Function":"GetAllMeasurements","Args":[""]}'], stdout=subprocess.PIPE)
    result.wait()
    try:
        out,err = result.communicate(timeout=3)
        print(out)
    except TimeoutExpired:
        print('error')

    utf8Result = out.decode('utf-8')
    pResult = json.loads(utf8Result.split("status:200 payload:")[1][1:-4].replace('\\',''))
    fResult = json.dumps(pResult)
    #print("final : %s", fResult)
    return {"Response": fResult}


@app.get("/measurements/{location}")
def getAllMeasurementsByLocation(location: str):
    fcnArgString = '{"Function":"QueryMeasurementsByLocation","Args":["' + location + '"]}'
    result = subprocess.Popen(["docker", "exec", "-t",  "cli",
     "peer", "chaincode", "invoke" ,"--tls", "--cafile", "/opt/home/managedblockchain-tls-chain.pem", "--channelID", "demchannel" ,"--name" ,"demcc" ,"-c",
     fcnArgString], stdout=subprocess.PIPE)
    result.wait()
    try:
        out,err = result.communicate(timeout=3)
        print(out)
    except TimeoutExpired:
        print('error')

    utf8Result = out.decode('utf-8')
    pResult = json.loads(utf8Result.split("status:200 payload:")[1][1:-4].replace('\\',''))
    fResult = json.dumps(pResult)
    #print("final : %s", fResult)
    return {"Response": fResult}


@app.put("/measurements/{location}/{cdn}/add")
def addMeasurement(location: str, cdn: str, measurement: Measurement):
    fcnArgString = '{"Function":"CreateMeasurement","Args":["' + \
        location + '", "' + \
        measurement.measuredepoch + '", "' + \
        measurement.rtt + '", "' + \
        measurement.cdn + '", "' + \
        measurement.provider + '"]}'
    result = subprocess.Popen(["docker", "exec", "-t",  "cli",
        "peer", "chaincode", "invoke" ,"--tls", "--cafile", "/opt/home/managedblockchain-tls-chain.pem", "--channelID", "demchannel" ,"--name" ,"demcc" ,"-c",
        fcnArgString], stdout=subprocess.PIPE)
    result.wait()
    try:
        out,err = result.communicate(timeout=3)
        print(out)
    except TimeoutExpired:
        print('error')

    utf8Result = out.decode('utf-8')
    pResult = json.loads(utf8Result.split("status:200 payload:")[1][1:-4].replace('\\',''))
    fResult = json.dumps(pResult)
    #print("final : %s", fResult)
    return {"Response": fResult}


@app.put("/measurements/{location}/{cdn}/update")
def updateMeasurement(location: str, cdn: str, measurement: Measurement):
    fcnArgString = '{"Function":"UpdateMeasurement","Args":["' + \
        location + '", "' + \
        measurement.measuredepoch + '", "' + \
        measurement.rtt + '", "' + \
        measurement.cdn + '", "' + \
        measurement.provider + '"]}'
    result = subprocess.Popen(["docker", "exec", "-t",  "cli",
        "peer", "chaincode", "invoke" ,"--tls", "--cafile", "/opt/home/managedblockchain-tls-chain.pem", "--channelID", "demchannel" ,"--name" ,"demcc" ,"-c",
        fcnArgString], stdout=subprocess.PIPE)
    result.wait()
    try:
        out,err = result.communicate(timeout=3)
        print(out)
    except TimeoutExpired:
        print('error')

    utf8Result = out.decode('utf-8')
    pResult = json.loads(utf8Result.split("status:200 payload:")[1][1:-4].replace('\\',''))
    fResult = json.dumps(pResult)
    #print("final : %s", fResult)
    return {"Response": fResult}


@app.put("/measurements/{location}/{cdn}/delete")
def deleteMeasurement(location: str, cdn: str):
    fcnArgString = '{"Function":"DeleteMeasurement","Args":["' + \
        location + '", "' + \
        cdn + '"]}'
    result = subprocess.Popen(["docker", "exec", "-t",  "cli",
        "peer", "chaincode", "invoke" ,"--tls", "--cafile", "/opt/home/managedblockchain-tls-chain.pem", "--channelID", "demchannel" ,"--name" ,"demcc" ,"-c",
        fcnArgString], stdout=subprocess.PIPE)
    result.wait()
    try:
        out,err = result.communicate(timeout=3)
        print(out)
    except TimeoutExpired:
        print('error')

    return {"Response": result}
