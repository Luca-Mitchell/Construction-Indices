

def excludeOutliers(data, blockSize):
    divisisions = (len(data) // blockSize) + 1
    total = 0
    blocks = []

    for i in range(divisisions):
        blocks.append(data[total:min(total+blockSize, len(data))])
        total += blockSize

    for block in blocks:
        avgIncrease = (block[len(block)-1] - block[0]) / len(block)
        cutoff = 1.5 * avgIncrease
        for i, item in enumerate(block):
            increase = block[i+1] - block[i]
            if increase > cutoff:
                del block [i+1]

    return [[item for item in block] for block in blocks]