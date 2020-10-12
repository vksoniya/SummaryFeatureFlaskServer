from redisChannelAccess import subscribeToRedisChannel
import json

#To Do:
#Solve Json parse error

def getcurrentMeetingInfo():
    meetingInfo = {}
    #Check redis channel to get current meeting info
    #channelName = "from-voice-conf-redis-channel"
    redisChannelMessage = subscribeToRedisChannel()

    for msg in redisChannelMessage:
        strData = str(msg['data'])
        try:
            dictData = json.loads(strData[2:-1])
            #print("Channel Envelope: " + str(dictData['envelope']))
            print("Channel Envelope Name: " + str(dictData['envelope']['name']))
            cEnvName = str(dictData['envelope']['name'])
            if cEnvName == "UserStatusVoiceConfEvtMsg":
                #print("Channel Core: " + str(dictData['core']))
                voiceConfID = dictData['envelope']['routing']['voiceConf']
                confRecordings = dictData['core']['body']['confRecordings'] 
                recordPath = confRecordings[0]['recordPath'] #Audio File .Opus Record path
                recordTimeStamp =  confRecordings[0]['recordStartTime'] #Audio File record timestamp
                print("Voice Conf ID: " + str(voiceConfID))
                print("Record Path:" + str(recordPath))
                print("Time Stamp: " + str(recordTimeStamp))

                #User List
                usrNames = []
                userList = dictData['core']['body']['confUsers']
                for usr in userList:
                    usrNames.append(str(usr['callerIdName']))
                
                meetingInfo = { 'voiceConfID' : str(voiceConfID), 'RecordPath': str(recordPath), 'recordTimeStamp' : str(recordTimeStamp), 'userNames' : usrNames }
                print("Meeting Information:" + str(meetingInfo))
                break
        except JSONDecodeError as e:
            print ("Decoding JSON has failed" + str(e))
            pass
        except AssertionError:
            pass
        finally:
            print ("We will continue for sure")
        
    return meetingInfo