from fulcrum.mixins import Findable, Deleteable, Createable, Searchable, Updateable, Downloadable
from . import BaseAPI


class Forms(BaseAPI, Findable, Deleteable, Createable, Searchable, Updateable):
    path = 'forms'


class Records(BaseAPI, Findable, Deleteable, Createable, Searchable, Updateable):
    path = 'records'

    def history(self, id):
        api_resp = api_resp = self.call('get', '{0}/{1}/history'.format(self.path, id))
        return api_resp

class Webhooks(BaseAPI, Findable, Deleteable, Createable, Searchable, Updateable):
    path = 'webhooks'


class Photos(BaseAPI, Findable, Searchable, Downloadable):
    path = 'photos'
    dl_ext = 'jpg'
    dl_sizes = ['thumbnail', 'large']


class Signatures(BaseAPI, Findable, Searchable):
    path = 'signatures'


class Videos(BaseAPI, Findable, Searchable, Downloadable):
    path = 'videos'
    dl_ext = 'mp4'
    dl_sizes = ['small', 'medium']


class Memberships(BaseAPI, Searchable):
    path = 'memberships'


class Roles(BaseAPI, Searchable):
    path = 'roles'


class ChoiceLists(BaseAPI, Findable, Deleteable, Createable, Searchable, Updateable):
    path = 'choice_lists'


class ClassificationSets(BaseAPI, Findable, Deleteable, Createable, Searchable, Updateable):
    path = 'classification_sets'


class Projects(BaseAPI, Findable, Deleteable, Createable, Searchable, Updateable):
    path = 'projects'


class Changesets(BaseAPI, Findable, Createable, Searchable, Updateable):
    path = 'changesets'

    def close(self, id):
        api_resp = api_resp = self.call('put', '{0}/{1}/close'.format(self.path, id))
        return api_resp


class ChildRecords(BaseAPI, Searchable):
    path = 'child_records'
