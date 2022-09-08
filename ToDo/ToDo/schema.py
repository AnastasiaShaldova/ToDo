import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from usersapp.models import Users
from taskapp.models import Project


# class Query(ObjectType):
#     hello = graphene.String(default_value='HI!')
#
#
# schema = graphene.Schema(query=Query)


# _________________________________________________________

class UserType(DjangoObjectType):
    class Meta:
        model = Users
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(ObjectType):

    user_by_id = graphene.List(UserType, id=graphene.Int(required=False))

    def resolve_user_by_id(root, info, id=None):
        if id:
            return Users.objects.get(id=id)
        return Users.objects.all()

    project_by_user = graphene.List(ProjectType, username=graphene.String(required=False))

    def resolve_project_by_user(root, info, first_name=None):
        if first_name:
            return Users.objects.filter(usersapp__first_name=first_name)
        return Users.objects.all()


# _________________________________________________________



class UserCreateMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = Users.objects.create(**kwargs)
        return cls(user=user)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = Users.objects.get(id=kwargs.get('id'))
        user.email = kwargs.get('email')
        user.save()
        return cls(user=user)

class UserDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    users = graphene.List(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        Users.objects.get(id=kwargs.get('id')).delete()
        return cls(users=Users.objects.all())


class Mutations(ObjectType):
    update_user = UserUpdateMutation.Field()
    create_user = UserCreateMutation.Field()
    delete_user = UserDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)