class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        
        totalStep = 0
        currentX = X[0]
        currentY = Y[0]
        for i in range(1, len(X)) :
            totalStep += max(abs(currentX - X[i] ), abs(currentY - Y[i]))
            currentX = X[i]
            currentY = Y[i]
        return totalStep

