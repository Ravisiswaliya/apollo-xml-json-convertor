from django.http import JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import xml.etree.ElementTree as ET


def xml_to_json(file):
    tree = ET.parse(file)
    root = tree.getroot()
    if len(root) > 0:
        res = [{child.tag: [{c.tag: c.text} for c in child]} for child in root]
        return res
    else:
        return {"Root": ""}


def upload_page(request):
    if request.method == "POST":
        # TODO: Convert the submitted XML file into a JSON object and return to the user.
        my_file = request.FILES["file"]  # getting file from html form
        fs = FileSystemStorage()
        filename = fs.save(my_file.name, my_file)  # saving file to media
        file_path = f"{settings.MEDIA_ROOT}/{filename}"  # preparing file path
        return JsonResponse(xml_to_json(file_path), safe=False)

    return render(request, "upload_page.html")
