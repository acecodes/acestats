import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies: ', len(table.records)

def live_births(table):
	firsts = survey.Pregnancies()
	others = survey.Pregnancies()

	for i in table.records:
		if i.outcome != 1:
			continue

		if i.birthord == 1:
			firsts.AddRecord(i)

		else:
			others.AddRecord(i)

	return firsts, others

if __name__ == '__main__':
	print live_births(table)