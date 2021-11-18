#!/usr/bin/env python

from TableIO import *
from pylab import *
from string import *

########### plot PDRs
if 0:

    PDRdirs = ['Bruderer-PDR_A/', 'KOSMAtau-Roellig/','Cloudy-Ferland-PDR/','Meudon-Le_Bourlot/',
               'UCL_PDR-Bell/','3D_UCL_PDR-Bisbas/','Wolfire-Kaufman/','ProDiMo-Thi-Woitke/', 'Meijerink-PDR/']

    PDRcols = ['r-', 'c-' ,'m--','g-',
               'b-',  'b--','y-','g--', 'm-']

    PDRmult = [1.0, 2*pi, 1.0, 2*pi,
               2*pi,  1.0, 1.0, 1.0, 1.0]

    panels = [1,2,4,5,6]
    label  = ['PDR1: n=3, X=1'  ,'PDR2: n=3, X=5',
              'PDR3: n=5.5, X=1','PDR4: n=5.5, X=5',
              'PDR5: n=7, X=1']

    # plot old data?
    old = 0
    # normalize?
    norm = 0
    # highest j?
    Jmax = 50
    # limits
    # PDRs1
    if norm == 0 and Jmax == 50:
        ylims = [[-25.2,0.8],[-14.2,-3],[-12.2,3.5],[-8.8,-2],[-19,5.8]]
    # PDRs2
    if norm == 0 and Jmax == 20:
        ylims = [[-13.2,-3.8],[-12.2,-3],[-9.2,-2.8],[-6.8,-2],[-10.2,-3.2]]
    # PDRs2-norm
    if norm == 1 and Jmax == 20:
        ylims = [[-7.2,2.4],[-4.4,3],[-2.6,2.8],[-0.8,4],[-3.2,2.4]]
    
    # read/plot PDRs
    for d in range(len(PDRdirs)):
        for i in range(5):
            lab = replace(PDRdirs[d],'-',' ')
            lab = replace(lab,'_',' ')
            lab = replace(lab,' PDR','')
            lab = lab[:-1]
            found = 0
            if old:
                file = PDRdirs[d]+'old/PDR'+str(i+1)+'-CO.txt'
                try:
                    J,CO = readColumns(file,'#',[0,1])
                except :
                    file = PDRdirs[d]+'PDR'+str(i+1)+'-CO.txt'
                    try:
                        J,CO = readColumns(file,'#',[0,1])
                    except :
                        print file+' does not exist'
                    else:
                        print 'plotting %s' % file 
                        found = 1
                else:
                    print 'plotting %s' % file 
                    found = 1
            else: #plot newest
                file = PDRdirs[d]+'PDR'+str(i+1)+'-CO.txt'
                try:
                    J,CO = readColumns(file,'#',[0,1])
                except :
                    print file+' does not exist'
                else:
                    found = 1

            if found:
                subplot(2,3,panels[i])
                title(label[i])
                if norm:
                    CO = array(CO)*PDRmult[d]
                    semilogy(J,array(CO)/CO[0],PDRcols[d],label=lab)
                else:
                    semilogy(J,array(CO)*PDRmult[d],PDRcols[d],label=lab)
                xlim(0,Jmax)
                ylim(10**ylims[i][0],10**ylims[i][1])


    xlab = 'Upper J-level'
    if norm:
        ylab = 'Normalized Flux'
    else:
        ylab = 'Flux [erg/s/cm2]'
    subplot(2,3,1)
    ylabel(ylab)
    subplot(2,3,4)
    ylabel(ylab)
    xlabel(xlab)
    subplot(2,3,5)
    xlabel(xlab)
    subplot(2,3,6)
    xlabel(xlab)
    
    from matplotlib.font_manager import FontProperties
    fontP = FontProperties()
    fontP.set_size('small')
    subplot(2,3,2)
    legend(loc='center left', bbox_to_anchor=(1.1, 0.5), prop = fontP)

    subplots_adjust(left  =0.12)
    subplots_adjust(bottom=0.10)
    subplots_adjust(right =0.98)
    subplots_adjust(top   =0.95)
    subplots_adjust(wspace=0.30)
    subplots_adjust(hspace=0.25)
            
    show()

########### plot XDRs
if 0:
    # XDRs only
    #XDRdirs = ['Cloudy-Ferland-XDR/','Bruderer-XDR/', 'Meijerink-XDR/', 'Woitke-ProDiMo-XDR/',]
     # shocks included
    XDRdirs = ['Cloudy-Ferland-XDR/','Bruderer-XDR/', 'Meijerink-XDR/', 'Woitke-ProDiMo-XDR/',
               'Kristensen_C_shock/', 'Kristensen_J_shock/']
   
    XDRcols = ['m-','r-','b-','c-',
               'g-','g--']

    XDRmult = [1.0, 1.0, 1.0,2*pi,
               1000.,1000.]

    label  = ['XDR1: n=3, FX=2.7'  ,'XDR2: n=3, FX=270',
              'XDR3: n=5.5, FX=2.7','XDR4: n=5.5, FX=270']


    label  = ['1: n=3, FX=2.7, v=10'  ,'2: n=3, FX=270, v=40',
              '3: n=5.5, FX=2.7, v=10','4: n=5.5, FX=270, v=40']


    panels = [1,2,4,5]

    # normalize?
    norm = 1
    # highest j?
    Jmax = 50
    
    # read/plot XDRs
    for d in range(len(XDRdirs)):
        for i in range(4):
            lab = replace(XDRdirs[d],'-',' ')
            lab = replace(lab,'_',' ')
            lab = replace(lab,' XDR','')
            lab = lab[:-1]
            file = XDRdirs[d]+'XDR'+str(i+1)+'-CO.txt'
            try:
                J,CO = readColumns(file,'#',[0,1])
            except :
                print file+' does not exist'
            else:
                subplot(2,3,panels[i])
                title(label[i])
                if norm:
                    CO = array(CO)*XDRmult[d]
                    semilogy(J,array(CO)/CO[0],XDRcols[d],label=lab)
                else:
                    CO = array(CO)*XDRmult[d]
                    semilogy(J,array(CO),XDRcols[d],label=lab)
                xlim(0,Jmax)

        #legend(loc=0)
    if 1:
        from matplotlib.font_manager import FontProperties
        fontP = FontProperties()
        fontP.set_size('medium')
        subplot(2,3,2)
        legend(loc='center left', bbox_to_anchor=(1.1, 0.5), prop = fontP)
     
    xlab = 'Upper J-level'
    if norm:
        ylab = 'Normalized Flux'
    else:
        ylab = 'Flux [erg/s/cm2]'
    subplot(2,3,1)
    ylabel(ylab)
    subplot(2,3,4)
    ylabel(ylab)
    xlabel(xlab)
    subplot(2,3,5)
    xlabel(xlab)

    subplots_adjust(left  =0.12)
    subplots_adjust(bottom=0.10)
    subplots_adjust(right =0.98)
    subplots_adjust(top   =0.95)
    subplots_adjust(wspace=0.30)
    subplots_adjust(hspace=0.25)
                            
    show()

############ plot line ratios for PDRs   
if 1:
    # plot x1/x2 vs y1/y2
    x1 = 18
    x2 = 1
    y1 = 18
    y2 = 6

    old = 1
    alph = 0.5
    XDRdirs = ['Cloudy-Ferland-XDR/','Bruderer-XDR/', 'Meijerink-XDR/', 'Woitke-ProDiMo-XDR/']
    XDRcols = ['co','cD','yo','yD']
    # read/plot XDRs
    for i in range(4):
        labeled = [0,0,0,0,0]
        avexl = []
        aveyl = []
        for d in range(len(XDRdirs)):
            file = XDRdirs[d]+'XDR'+str(i+1)+'-CO.txt'
            try:
                J,CO = readColumns(file,'#',[0,1])
            except :
                print file+' does not exist'
            else:
                try:
                    loglog([CO[x1-1]/CO[x2-1]],[CO[y1-1]/CO[y2-1]],XDRcols[i],label='__nolegend__',alpha=alph)
                except IndexError:
                    pass
                else:
                    print 'plotting %s' % file
                    avexl.append(log10(CO[x1-1]/CO[x2-1]))
                    aveyl.append(log10(CO[y1-1]/CO[y2-1]))
        avex = sum(avexl)/len(avexl)
        avey = sum(aveyl)/len(aveyl)
        loglog([10**avex],[10**avey],XDRcols[i],label='XDR'+str(i+1),markersize=10,zorder=10)

    PDRdirs = ['Bruderer-PDR_A/','Bruderer-PDR_B/','Bruderer-PDR_C/','Bruderer-PDR_Bench/', 'KOSMAtau-Roellig/',
               'Cloudy-Ferland-PDR/','Meudon-Le_Bourlot/','UCL_PDR-Bell/','3D_UCL_PDR-Bisbas/',
               'Wolfire-Kaufman/','ProDiMo-Thi-Woitke/', 'Meijerink-PDR/']

    PDRcols = ['ro','rD','bo','bD','mo']

    # read/plot PDRs
    for i in range(4):
        labeled = [0,0,0,0,0]
        avexl = []
        aveyl = []
        for d in range(len(PDRdirs)):
            found = 0
            if old:
                file = PDRdirs[d]+'old/PDR'+str(i+1)+'-CO.txt'
                try:
                    J,CO = readColumns(file,'#',[0,1])
                except :
                    file = PDRdirs[d]+'PDR'+str(i+1)+'-CO.txt'
                    try:
                        J,CO = readColumns(file,'#',[0,1])
                    except :
                        print file+' does not exist'
                    else:
                        print 'plotting %s' % file 
                        found = 1
                else:
                    print 'plotting %s' % file 
                    found = 1
            else: #plot newest
                file = PDRdirs[d]+'PDR'+str(i+1)+'-CO.txt'
                try:
                    J,CO = readColumns(file,'#',[0,1])
                except :
                    print file+' does not exist'
                else:
                    found = 1
            if found:
                try:
                    loglog([CO[x1-1]/CO[x2-1]],[CO[y1-1]/CO[y2-1]],PDRcols[i],label='__nolegend__',alpha=alph)
                except IndexError:
                    pass
                else:
                    print 'plotting %s' % file
                    avexl.append(log10(CO[x1-1]/CO[x2-1]))
                    aveyl.append(log10(CO[y1-1]/CO[y2-1]))
        avex = sum(avexl)/len(avexl)
        avey = sum(aveyl)/len(aveyl)
        loglog([10**avex],[10**avey],PDRcols[i],label='PDR'+str(i+1),markersize=10,zorder=10)

     
    legend(loc=0,numpoints=1)
    xlabel('CO(%i-%i)/CO(%i-%i)' % (x1,x1-1,x2,x2-1) ) 
    ylabel('CO(%i-%i)/CO(%i-%i)' % (y1,y1-1,y2,y2-1) ) 
    show()

########## plot peaks
if 0:
    PDRdirs = ['Bruderer-PDR_A/', 'KOSMAtau-Roellig/','Cloudy-Ferland-PDR/','Meudon-Le_Bourlot/',
               'UCL_PDR-Bell/','3D_UCL_PDR-Bisbas/','Wolfire-Kaufman/','ProDiMo-Thi-Woitke/', 'Meijerink-PDR/']
    old =0
    for j in range(4):
        i = [1,3,0,2][j]
        subplot(2,2,i+1)
        Jmaxs = list(zeros(30))
        for d in range(len(PDRdirs)):
            found = 0
            if old:
                file = PDRdirs[d]+'old/PDR'+str(i+1)+'-CO.txt'
                try:
                    J,CO = readColumns(file,'#',[0,1])
                except :
                    file = PDRdirs[d]+'PDR'+str(i+1)+'-CO.txt'
                    try:
                        J,CO = readColumns(file,'#',[0,1])
                    except :
                        print file+' does not exist'
                    else:
                        print 'plotting %s' % file 
                        found = 1
                else:
                    print 'plotting %s' % file 
                    found = 1
            else: #plot newest
                file = PDRdirs[d]+'PDR'+str(i+1)+'-CO.txt'
                try:
                    J,CO = readColumns(file,'#',[0,1])
                except :
                    print file+' does not exist'
                else:
                    found = 1
            if found:
                Jmax = list(CO).index(max(CO))
                Jmaxs[Jmax+1]+=1
        plot(range(30),Jmaxs,'b-',drawstyle='steps-mid',lw=2)
        maxmax = Jmaxs.index(max(Jmaxs))
        plot([maxmax,maxmax],[0,5],'r--',lw=2)
        text(12,4,'PDR%i'%(i+1))
        xlim(1,15)
        ylim(0,4.8)
        legend(loc=0)
        xlabel('J turnover')
        ylabel('#')
        
    subplots_adjust(wspace=0.0)
    subplots_adjust(hspace=0.0)
    show()
        
