class ConfigManager(object):
    """
        Class to provide the configuration details
    """

    url = "http://10.235.112.35:5003/api/v2/nlu/predict"
    sop_predict_url = "http://10.235.112.36:8021/api/v1/sopsync/predict/"
    chatbot_url ="http://10.235.112.34:5003/HolmesIT/chatbot/v2/api"
    classifier_url = "http://10.235.112.36:8024/api/v1/Classifier/verifyAugBot"
    cogminer_url = "http://10.235.112.36:8090/api/v2/CogMiner/predict"
    nlu_url = "http://10.235.112.35:4000/api/v1/nlu/predict"
