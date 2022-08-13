import random as rm

import cadquery as cq
from cadquery import exporters
a=0
for i in range(3500):
    n0=rm.randint(-5,5)
    n=rm.randint(-4,4)

    s = cq.Workplane("XY")
    sPnts = [
        (n0, 1.5),
        (1.0, n),
        (-n, 1.0),
        (0, -n0)
    ]
 
    #//////////////////////////////////////////////////
    n11=rm.randint(-5,5)
    n1=rm.randint(-4,4)
    s1 = cq.Workplane("XY")
    sPnts1 = [
        (n11, 1.5),
        (1.0, n1),
        (-n1, 1.0),
        (0, -n11)
    ]

    #////////////////////////////////////////////////////

    n12=rm.randint(-5,5)
    n2=rm.randint(-4,4)
    s2 = cq.Workplane("XY")
    sPnts2 = [
        (n12, 1.5),
        (1.0, n2),
        (-n2, 1),
        (0, -n12)
    ]
 
    #///////////////////////////////////////////////////////

    n13=rm.randint(-4,4)
    n3=rm.randint(-3,3)
    s3 = cq.Workplane("XY")
    sPnts3 = [
        (n13, 1.5),
        (1.0, n3),
        (-n3, 1.0),
        (0, -n13)
    ]
    #////////////////////////////////////////////////////

    n14=rm.randint(-2,2)
    n4=rm.randint(-1,1)
    s4 = cq.Workplane("XY")
    sPnts4 = [
        (n14, 1.5),
        (1.0, n4),
        (-n4, 1),
        (0, -n14)
    ]
   

    try:
        result = (cq.Workplane("front").box(10,10.0, 0.125).pushPoints([(0, 0.75), (0, -0.75)])
            .polyline(sPnts, includeCurrent=True).close().cutThruAll())

        result1 = (cq.Workplane("front").box(8, 8.0, 0.25).pushPoints([(0, 0.75), (0, -0.75)])
            .polyline(sPnts1, includeCurrent=True).close().cutThruAll())

        result2 = (cq.Workplane("front").box(6.0, 6.0, 0.5).pushPoints([(0, 0.75), (0, -0.75)])
            .polyline(sPnts2, includeCurrent=True).close().cutThruAll())

        result3 = (cq.Workplane("front").box(4.0, 4.0, 1.0).pushPoints([(0, 0.75), (0, -0.75)])
            .polyline(sPnts3, includeCurrent=True).close().cutThruAll())


        result4 = (cq.Workplane("front").box(2.0, 2.0, 2).pushPoints([(0, 0.75), (0, -0.75)])
            .polyline(sPnts4, includeCurrent=True).close().cutThruAll())

        assy=cq.Assembly()
        assy.add(result4,
            name="cone0",
            color=cq.Color("azure")
        )
        assy.add(result3, name="cone1", color=cq.Color("azure2"))
        assy.add(result2, name="cone2",color=cq.Color("azure3"))
        assy.add(result1, name="cone3",color=cq.Color("azure4"))
        assy.add(result, name="cone4",color=cq.Color("white"))
        
        if a<10:
            assy.save(f'MetaGeo#00{a}.step')
        elif a>=10 or a<100:
            assy.save(f'MetaGeo#0{a}.step')
        else:
            assy.save(f'MetaGeo#{a}.step')
        a+=1

        if a==501:
            break

    except Exception as e:
          print(e)
