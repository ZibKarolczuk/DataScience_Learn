# IMPORTING PACKAGES
import numpy as np
import scipy
import scipy.spatial
from scipy.spatial import distance_matrix
import matplotlib
import matplotlib.pyplot as plt
import time

# DECLARING FUNCTIONS:
def makeImportantVariables(groups = 3, randomPointsInEveryGroup = 12):
    return groups, randomPointsInEveryGroup

def generateOtherVariables():
    scatters = randomPointsInEveryGroup * 4
    indexes = np.arange(scatters)
    np.random.shuffle(indexes)
    indexes = indexes[:groups]
    iteration = 1
    doIterate = True
    return scatters, indexes, iteration, doIterate

def makeRandomPoints():
    a1_x = np.random.uniform(3,17,randomPointsInEveryGroup)
    a1_y = np.random.uniform(3,17,randomPointsInEveryGroup)
    a2_x = np.random.uniform(0,13,randomPointsInEveryGroup)
    a2_y = np.random.uniform(0,13,randomPointsInEveryGroup)
    a3_x = np.random.uniform(7,20,randomPointsInEveryGroup)
    a3_y = np.random.uniform(7,20,randomPointsInEveryGroup)
    r4_x = np.random.uniform(0,20,randomPointsInEveryGroup)
    r4_y = np.random.uniform(0,20,randomPointsInEveryGroup)
    points_x = np.r_[a1_x, a2_x, a3_x, r4_x].reshape(-1,1)
    points_y = np.r_[a1_y, a2_y, a3_y, r4_y].reshape(-1,1)
    points = np.hstack((points_x, points_y))
    return points_x, points_y, points

def linkingRandomScattersWithTheNearestScatters():
    distances = scipy.spatial.distance_matrix(points, points)
    linkLines = np.array([])
    for x in range(scatters):
        i = indexes[np.argmin(distances[x][indexes])]
        linkLines = np.append(linkLines, np.r_[points[x], points[i]])
    linkLines = linkLines.reshape(-1, 4)
    return linkLines

def linkingCentresFromPreviousIterationWithTheNearestScatters():
    distances = scipy.spatial.distance_matrix(points, groupsCentres)
    linkLines = np.array([])
    for i in range(len(distances)):
        i_min = np.argmin(distances[i])
        linkLines = np.append(linkLines, np.r_[points[i], groupsCentres[i_min]])
    linkLines = linkLines.reshape(-1, 4)
    return linkLines

def findingCentresOfInitialGroups():
    centres = np.array([])
    for i in indexes:
        group = linkLines[np.where(linkLines[:,2] == points[i][0])]
        centres = np.append(centres, group.mean(0))
    return getCentresVectors(centres)

def findingCentresOfRecalculatedGroups(groupsCentresFromPreviousIteration):
    centres = np.array([])
    for i in range(len(groupsCentresFromPreviousIteration)):
        group = linkLines[np.where(linkLines[:,2] == groupsCentresFromPreviousIteration[i][0])]
        centres = np.append(centres, group.mean(0))
    return getCentresVectors(centres)

def getCentresVectors(centres_raw):
    centres = centres_raw.reshape(-1,4)
    groupsCentres = np.hstack((centres[:,[0]], centres[:,[1]])).reshape(-1,2)
    return centres, groupsCentres

def doNextIteration():
    matchVectors = np.hstack((np.abs(np.r_[centres[:,[2]] - centres[:,[0]]]) < 0.001,
                              np.abs(np.r_[centres[:,[2]] - centres[:,[0]]]) < 0.001))
    return ~np.all(matchVectors)

def plotScattersOnly():
    plt.title(str(scatters) + " random scatters in "+ str(groups) + " groups")
    plt.plot(points_x, points_y, 'o', alpha=0.3)
    plt.axis('equal')
    plt.show()

def prepPlottingMoreIterations():
    plt.plot(groupsCentres[:,0], groupsCentres[:,1], 'bo', alpha=0.8)

def plotCurrentIteration():
    plt.title("Centres of " + str(groups) + " groups (" + str(scatters) + " scatters) - iteration " + str(iteration))
    plt.plot(points_x, points_y, 'o', alpha=0.3)
    plt.plot(np.r_[linkLines[:,0], linkLines[:,2]].reshape(-1,scatters),
             np.r_[linkLines[:,1], linkLines[:,3]].reshape(-1,scatters), 'y-', alpha=0.25)
    # for i in range(points.shape[0]):
    #     plt.text(points[i,0], points[i,1], str(i), alpha=0.5)
    plt.plot(centres[:,0], centres[:,1], 'ro', alpha=0.8)
    plt.axis('equal')
    plt.show()


# CALCULATING IMPORTANT VARIABLES:
groups, randomPointsInEveryGroup = makeImportantVariables(3,12)
scatters, indexes, iteration, doIterate = generateOtherVariables()

# GENERATING VECTORS OF RANDOM POINTS:
points_x, points_y, points = makeRandomPoints()

# PLOTTING SCATTERS:
plotScattersOnly()

# INITIAL CALCULATION:
linkLines = linkingRandomScattersWithTheNearestScatters()
centres, groupsCentres = findingCentresOfInitialGroups()
plotCurrentIteration()

# ITERATIONS FINDING CENTRES OF GROUPS:
while (doIterate):
    iteration += 1
    prepPlottingMoreIterations()
    linkLines = linkingCentresFromPreviousIterationWithTheNearestScatters()
    centres, groupsCentres = findingCentresOfRecalculatedGroups(groupsCentres)
    plotCurrentIteration()
    doIterate = doNextIteration()
