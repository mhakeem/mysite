from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Poll, Choice
from django.template import Context, loader, RequestContext

# def index(request):
# 	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
# 	# output = ', '.join([p.question for p in latest_poll_list])
# 	# return HttpResponse(output)
# 	# t = loader.get_template('polls/index.html')
# 	# c = Context({
# 	# 		'latest_poll_list':latest_poll_list
# 	# 	})
# 	# return HttpResponse(t.render(c))
# 	return render_to_response('polls/index.html', {'latest_poll_list':latest_poll_list})

# def detail(request, poll_id):
# 	# return HttpResponse("You're looking at poll %s." % poll_id)
# 	# try:
# 	# 	p = Poll.objects.get(pk=poll_id)
# 	# except Poll.DoesNotExist:
# 	# 	raise Http404
# 	p = get_object_or_404(Poll, pk=poll_id)
# 	return render_to_response('polls/detail.html', {'poll': p}, 
# 		context_instance=RequestContext(request))

# def results(request, poll_id):
# 	# return HttpResponse("You're looking at the results of poll %s." % poll_id)
# 	p = get_object_or_404(Poll, pk=poll_id)
# 	return render_to_response('polls/results.html', {'poll': p})

def vote(request, poll_id):
	# return HttpResponse("You're voting on poll %s." % poll_id)
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the poll voting form.
		return render_to_response('polls/detail.html', {
	    	'poll': p,
	    	'error_message': "You didn't select a choice.",
		}, context_instance=RequestContext(request))
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		# return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
		return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))


