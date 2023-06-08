import random
import matplotlib.pyplot as plt
import numpy as np


def pointCreate(points):
    return points.append([random.uniform(0, 1), random.uniform(0, 1)])


def pointSpaceFill(amount):
    points = []
    while amount > len(points):
        pointCreate(points)
    return points


def measureCalculating(firstX, firstY, secondX, secondY):
    return np.sqrt((secondX - firstX) ** 2 + (secondY - firstY) ** 2)


def comparisonClusters(measures):
    min, i, index = measures[0], 1, 0
    for i in range(len(measures)):
        if measures[i] < min:
            min = measures[i]
            index = i
    return index


def clustering(points, centers, amount, clusterAmount):
    clusters, num = [[] for i in range(clusterAmount)], 0
    while num < amount:
        measures = []
        for i in range(clusterAmount):
            measures.append(measureCalculating(points[num][0], points[num][1], centers[i][0], centers[i][1]))
        clusters[comparisonClusters(measures)].append(points[num])
        num += 1
    return clusters


def newCenterFindingMeans(cluster):
    sumX, sumY = 0, 0
    for i in range(len(cluster)):
        sumX += cluster[i][0]
        sumY += cluster[i][1]
    return [sumX / len(cluster), sumY / len(cluster)]


def kMeansClustering(points, clusterAmount):
    N = len(points)
    clusterCenters = [points[random.randint(0, N - 1)] for _ in range(clusterAmount)]

    while True:
        clusters = clustering(points, clusterCenters, N, clusterAmount)
        newCenters = [newCenterFindingMeans(cluster) for cluster in clusters]

        if newCenters == clusterCenters:
            break

        clusterCenters = newCenters

    return clusters, clusterCenters


def hierarchicalClustering(points, clusterAmount):
    N = len(points)
    clusterCenters = [points[random.randint(0, N - 1)] for _ in range(clusterAmount)]

    while True:
        clusters = clustering(points, clusterCenters, N, clusterAmount)
        newCenters = [newCenterFindingMeans(cluster) for cluster in clusters]

        if newCenters == clusterCenters:
            break

        clusterCenters = newCenters

    return clusters, clusterCenters


def createKMeansClusteringGraph(clusters, centers):
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.set_title("K-середніх", fontsize=18)
    plt.grid(True)
    for i in range(len(clusters)):
        color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        for j in range(len(clusters[i])):
            ax.scatter(clusters[i][j][0], clusters[i][j][1], color=color, s=10)
        ax.scatter(centers[i][0], centers[i][1], color='black', marker='o', s=100)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


def createHierarchicalClusteringGraph(clusters, centers):
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.set_title("Ієрархічний метод", fontsize=18)
    plt.grid(True)
    for i in range(len(clusters)):
        color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        for j in range(len(clusters[i])):
            ax.scatter(clusters[i][j][0], clusters[i][j][1], color=color, s=10)
        ax.scatter(centers[i][0], centers[i][1], color='black', marker='o', s=100)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


N, K = 1000, 13

pointSpace = pointSpaceFill(N)

kMeansClusters, kMeansClusterCenters = kMeansClustering(pointSpace, K)
hierarchicalClusters, hierarchicalClusterCenters = hierarchicalClustering(pointSpace, K)

createKMeansClusteringGraph(kMeansClusters, kMeansClusterCenters)
createHierarchicalClusteringGraph(hierarchicalClusters, hierarchicalClusterCenters)
