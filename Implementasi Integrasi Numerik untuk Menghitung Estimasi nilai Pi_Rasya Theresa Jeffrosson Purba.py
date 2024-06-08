import numpy as np
import time
import matplotlib.pyplot as plt

def calculateFunction(x):
    return 4 / (1 + x**2)

def simpson13Integration(a, b, numberOfSegments):
    h = (b - a) / numberOfSegments
    xValues = np.linspace(a, b, numberOfSegments + 1)
    yValues = calculateFunction(xValues)
    integralSum = yValues[0] + yValues[-1]

    for i in range(1, numberOfSegments, 2):
        integralSum += 4 * yValues[i]
    for i in range(2, numberOfSegments, 2):
        integralSum += 2 * yValues[i]

    return (h / 3) * integralSum

def rootMeanSquareError(estimatedValue, referenceValue):
    return np.sqrt(np.mean((estimatedValue - referenceValue)**2))

def main():
    referencePi = 3.14159265358979323846
    numberOfSegmentsValues = [10, 100, 1000, 10000]
    results = []

    for numberOfSegments in numberOfSegmentsValues:
        startTime = time.time()
        estimatedPi = simpson13Integration(0, 1, numberOfSegments)
        endTime = time.time()
        
        error = rootMeanSquareError(estimatedPi, referencePi)
        executionTime = endTime - startTime
        
        results.append((numberOfSegments, estimatedPi, error, executionTime))
        print(f"N = {numberOfSegments}: Estimated π = {estimatedPi}, RMS Error = {error}, Execution Time = {executionTime:.10f} seconds")

    return results

def plotResults(results):
    numberOfSegmentsValues = [result[0] for result in results]
    estimatedPis = [result[1] for result in results]
    errors = [result[2] for result in results]
    executionTimes = [result[3] for result in results]

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.plot(numberOfSegmentsValues, estimatedPis, 'o-', label='Estimated π')
    plt.axhline(y=3.14159265358979323846, color='r', linestyle='--', label='Reference π')
    plt.xscale('log')
    plt.xlabel('Number of Segments')
    plt.ylabel('Estimated π')
    plt.legend()
    plt.title('Estimated π vs Number of Segments')

    plt.subplot(1, 3, 2)
    plt.plot(numberOfSegmentsValues, errors, 'o-', label='RMS Error')
    plt.xscale('log')
    plt.xlabel('Number of Segments')
    plt.ylabel('RMS Error')
    plt.legend()
    plt.title('RMS Error vs Number of Segments')

    plt.subplot(1, 3, 3)
    plt.plot(numberOfSegmentsValues, executionTimes, 'o-', label='Execution Time (s)')
    plt.xscale('log')
    plt.xlabel('Number of Segments')
    plt.ylabel('Execution Time (s)')
    plt.legend()
    plt.title('Execution Time vs Number of Segments')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    mainResults = main()
    plotResults(mainResults)
