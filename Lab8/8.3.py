def dict3():
    empdata = {('ce', 77): 50000, ('ce', 277): 50000, ('ce', 177): 55000, ('ce', 12): 50000, ('design', 7): 5000}
    deptdata = {}

    for k, v in empdata.items():

        print(k[0], k[1], v)
        
        
        if k[0] not in deptdata:
            deptdata[k[0]] = {'Max': v, 'Min': v, 'Total': v}
        else:
       
            if v > deptdata[k[0]]['Max']:
                deptdata[k[0]]['Max'] = v
            elif v < deptdata[k[0]]['Min']:
                deptdata[k[0]]['Min'] = v
            deptdata[k[0]]['Total'] += v

   
    print(deptdata)

dict3()
