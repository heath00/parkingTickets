import plotly
import plotly.graph_objs as go
# from plotly.graph_objs import Bar, Layout
import numpy as np
from Ticket import ticket


# parseData
# takes in a raw text file and makes a dictionary of ticket Structures out of it
def parseData(txt_file):
	f = open(txt_file, "r")
	ticketDict = {}
	for line in f:
		tix = line
		tix = tix.split(',')
		newTicket = ticket(tix[0], tix[1], float(tix[2])+2.95)
		ticketDict[tix[0]] = newTicket
	return ticketDict


# writeNewTicket
# takes data from the web and writes it into a text file formatted for use with the grapher
def writeNewTicket(txt_file, new_tickets):
	f = open(txt_file, "a")
	for t in new_tickets:
		f.write(t.ticketNumber + "," + t.date + "," + t.amount + "\n")


		
#graph
#takes in a raw text file and creates a javascript graph out of it in the default browser using plotly
def graph(txt_file):
	ticketDict = parseData(txt_file)
	datesAndAmounts = {}

	#for every ticket in the dictionary, update the datesAndAmounts dict to graph it
	for k in ticketDict:
		item = ticketDict[k]
		# if the date is already in the dictionary, just add to that month's amount
		if item.date in datesAndAmounts:
			datesAndAmounts[item.date] += item.amount
		#otherwise, add it to the dictionary
		else:
			datesAndAmounts[item.date] = item.amount

	#get the dates and amounts into x and y to be passed into plotter
	dates = []
	cash = []
	hoverText = []
	colors = []

	for m in datesAndAmounts:
		cost = datesAndAmounts[m]
		dates.append(m)
		cash.append(cost)
		hoverText.append("You saved $" + "%.2f" % (80 - datesAndAmounts[m]) + " this month.")
		if cost > 80:
			colors.append('rgb(222,45,38)')
		else:
			colors.append('rgb(204,204,204)')


	trace0 = go.Bar(
				x=dates,
				y=cash,
				text=hoverText,
				marker=dict(
					color=colors
					),

		)

	data = [trace0]
	layout = go.Layout(
		title="Parking Ticket Costs by Month",
		xaxis=dict(
			title="Month"
			),
		yaxis=dict(
			title="Cost"
			),
	)
	fig = go.Figure(data=data, layout=layout)
	plotly.offline.plot(fig, filename='ticketCosts.html')
	
