from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserInfo
from .serializer import UserInfoSerializer
import joblib
import numpy as np


class IndexView(APIView):

    def get(self, request):
        return Response('You are in the home page', status=200)

    def post(self, request):
        getdata = request.data["Name"]

        userdata = UserInfo.objects.filter(Name=getdata)
        serializeddata = UserInfoSerializer(userdata, many=True)

        return Response(serializeddata.data, status=200)


class DataforPrediction(APIView):

    def get(self, request):
        return Response("Please add your data for prediction")

    def post(self, request):

        orginalinput = request.data
        inputdata = []
        for key in orginalinput.keys():
            if key != "Name":
                inputdata.append(orginalinput[key])
            continue
        inputdata = np.array(inputdata)
        inputdata = inputdata.reshape(1, -1)

        # model_file_path = "DrugPredictionProject/Decision_tree.joblib" # for local run
        model_file_path = "Decision_tree.joblib"  # for container run
        model = joblib.load(model_file_path)
        prediction = model.predict(inputdata)

        orginalinput['Prediction'] = str(prediction)

        serializer_class = UserInfoSerializer(data=orginalinput)

        if serializer_class.is_valid():
            serializer_class.save()
            print(serializer_class.errors)
            return Response(serializer_class.data)
        return Response('Data not saved')



# {
#     "Name": "Mubin"
# }
#47	M	LOW	HIGH	13.093
{
    "Name": "Mubin",
    "Age": 47,
    "Sex": 1,
    "BP": 2,
    "Cholesterol": 0,
    "Na_to_K": 13.093
}