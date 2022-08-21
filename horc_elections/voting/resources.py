from import_export import resources ,fields
from import_export.widgets import ManyToManyWidget
from .models import Candidate, Post, VoterList, Vote

class Candidate_Resource(resources.ModelResource):
    class Meta:
        model = Candidate
        fields = ("email", "name","hostel")
        export_order = ("email", "name","hostel")
        import_id_fields = ("email",)

class Post_Resource(resources.ModelResource):
    candidates = fields.Field(column_name='candidates', attribute='candidates', widget=ManyToManyWidget(model=Candidate,field='email',separator=','))
    class Meta:
        model = Post
        exclude = ('id',)
        import_id_fields = ("hostel","post_name")
        fields = ("hostel", "post_name","candidates_email")

        

class VoterList_Resource(resources.ModelResource):
    class Meta:
        model = VoterList
        fields = ("email", "hostel","voted")
        export_order = ("email", "hostel","voted")
        import_id_fields = ("email",)

class Vote_Resource(resources.ModelResource):
    class Meta:
        model = Vote
        fields = ("user", "post_id","vote_casted")
        export_order = ("user", "post_id","vote_casted")