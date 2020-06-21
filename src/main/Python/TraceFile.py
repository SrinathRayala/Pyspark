import logging,os
logging.basicConfig(filename='myprogramLog.txt',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.warning)
logging.debug('Start of Program')
#try:
#    raise Exception('This is the error message.')
#except:
 #   errorFile = open('error log.txt','a')
  #  errorFile.write(traceback.format_exc())
   # errorFile.close()
    #print('The traceback info')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total=1
    for i in range (1,n+1):
        total *= i
        logging.debug('i is %s,total is %s'%(i,total))
    logging.debug('Return value is %s' % (total))
    return total
print(factorial(5))
print(os.getcwd())
logging.debug('End of Program')