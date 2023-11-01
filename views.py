
from django.db.models import Q
from kernel.http import Response
from feeling.models import Feeling
from feeling.libs import load_or_create_feel
from profiles.models import Profile
from profiles.decorators import load_profile
import json

@load_profile
def load(request: object): 
    """
        @description:
    """
    res = Response()
    jsonQuery = json.loads(request.POST.get('jsonQuery'))
    query = Q(
        profile=request.profile
    )

    for relatedModel in jsonQuery:
        appendQuery = Q(relatedModel=relatedModel)
        for relatedModelId in jsonQuery[relatedModel]['relatedModelListId']:
            appendQuery |= Q(relatedModelId=relatedModelId)

        query &= appendQuery

    dbFeelingList = Feeling.objects.filter(query)
    res.feeling = {}
    for dbFeeling in dbFeelingList:
        if dbFeeling.relatedModel not in res.feeling:
            res.feeling[dbFeeling.relatedModel] = []
        res.feeling[dbFeeling.relatedModel].append(dbFeeling.serialize(request))
    return res.success()


@load_profile
def like(request: object):
    """
        @description:
    """
    res = Response()
    relatedModel = request.POST.get('relatedModel')
    relatedModelId = request.POST.get('relatedModelId')
    dbFeeling = load_or_create_feel(
        relatedModel, 
        relatedModelId,
        request.profile
    )
    dbFeeling.like_or_dislike = 1
    dbFeeling.save()

    res.feeling = dbFeeling.serialize(request)
    return res.success()

@load_profile
def dislike(request: object):
    """
        @description:
    """
    res = Response()
    relatedModel = request.POST.get('relatedModel')
    relatedModelId = request.POST.get('relatedModelId')
    dbFeeling = load_or_create_feel(
        relatedModel, 
        relatedModelId,
        request.profile,
    )
    dbFeeling.like_or_dislike = 0
    dbFeeling.save()

    res.feeling = dbFeeling.serialize(request)
    return res.success()