# if request.method == 'POST':
#     water_sample_form = Form1(request.POST)


#     aluminum = float(request.POST['aluminum'])
#     ammonia = float(request.POST['ammonia'])
#     arsenic = float(request.POST['arsenic'])
#     barium = float(request.POST['barium'])
#     cadmium = float(request.POST['cadmium'])
#     chloramine = float(request.POST['chloramine'])
#     chromium = float(request.POST['chromium'])
#     copper = float(request.POST['copper'])
#     flouride = float(request.POST['fluoride'])
#     bacteria = float(request.POST['bacteria'])
#     viruses = float(request.POST['viruses'])
#     lead = float(request.POST['lead'])
#     nitrates = float(request.POST['nitrates'])
#     nitrites = float(request.POST['nitrites'])
#     mercury = float(request.POST['mercury'])
#     perchl = float(request.POST['perchlorate'])
#     radium = float(request.POST['radium'])
#     selen = float(request.POST['selenium'])
#     silver = float(request.POST['silver'])
#     uranium = float(request.POST['uranium'])
#     feature_list = [aluminum, ammonia, arsenic, barium,
#                     cadmium, chloramine, chromium, copper,
#                     flouride, bacteria, viruses, lead,
#                     nitrates, nitrites, mercury, perchl,
#                     radium, selen, silver, uranium]
#     pred_result = getPredictions([feature_list])

#     context = {
#         'result': pred_result
#     }