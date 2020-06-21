def isComplete(order, ordersCompletedCount, ordersNonCompletedCount):
    isCompleted=order.split(",")[3] == "COMPLETE" or order.split(",")[3] == "CLOSED"
    if(isCompleted):
        ordersCompletedCount =ordersCompletedCount.add(1)
    else:
        ordersNonCompletedCount =ordersNonCompletedCount.add(1)
        return isCompleted