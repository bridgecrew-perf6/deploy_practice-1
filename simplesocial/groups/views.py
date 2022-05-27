from distutils.log import Log
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from groups.models import Group, GroupMember


class CreateGroupView(LoginRequiredMixin, generic.CreateView):
    model = Group  
    fields = ('name', 'description')
    

class SingleGroupView(generic.DetailView):
    model = Group
    template_name = 'groups/group_detail.html'
    context_object_name = 'group'


class ListGroupsView(generic.ListView):
    model = Group
    template_name = 'groups/group_list.html'
    context_object_name = 'object_list'
    


class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})
    
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except:
            messages.warning(self.request, 'Warning already a member!')
        else:
            messages.success(self.request, 'You are now a member!')

        return super().get(request, *args, **kwargs)



class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try: 
            membership = GroupMember.objects.filter(user=self.request.user, group__slug=self.kwargs.get('slug'))
        except:
            messages.warning(self.request, 'Sorry you are not in this Group!')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the Group!')

        return super().get(request, *args, **kwargs)