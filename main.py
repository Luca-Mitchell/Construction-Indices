import utils.FileHandler as f
import utils.DataManipulation as d
import utils.GraphHandler as g
import utils.EmailHandler as e

spreadsheet = f.scrapeSpreadsheet('https://www.ons.gov.uk/file?uri=/businessindustryandtrade/constructionindustry/datasets/interimconstructionoutputpriceindices/current/bulletindataset9.xlsx')

data = f.extractData(
    spreadsheet,
    'New work',
    [1, 4, 7, 10, 13, 16],
    ['Housing index, 2015=100', 'Infrastructure index, 2015=100', 'Public index, 2015=100', 'Private industrial index, 2015=100', 'Private commercial index, 2015=100', 'All new work index, 2015=100']
)

for header, content in data.items():
    data[header] = d.excludeOutliers(data[header], 10)

dates = g.genDates(len(data[list(data.keys())[0]]), 2014)

g.drawGraph('Housing index, 2015=100', dates, data['Housing index, 2015=100'])