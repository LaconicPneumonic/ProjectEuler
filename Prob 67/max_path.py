import argparse as ap
import sys

def parse_args(raw_args):
	parser = ap.ArgumentParser(
    prog="MaxPath"
	)

	parser.add_argument("-p","--path",default="triangle1.txt", type=str)
	return parser.parse_args(raw_args)

def load_triangle(path):
	""" takes path as input and outputs dictionary with format (r,c) : [num, bestpath]"""
	lst_triangle = 	open(path,"r").read().split("\n")

	triangle, row  = {} ,0
	for line in lst_triangle:
		colum = 0
		for num in line.split():
			#assign coordinate to list of num and max path
			triangle[(row,colum)] = [int(num),0]
			colum +=1
		row += 1

	triangle[(0,0)][1] = triangle[(0,0)][0]

	return triangle , row

def run(args):
	triangle , max_row = load_triangle(args.path)

	for row in xrange(1,max_row):
		triangle[row,0][1] = triangle[row-1,0][1] + triangle[row,0][0]
		triangle[row,row][1] = triangle[row-1,row-1][1] + triangle[row,row][0]
		for i in xrange(1, row):			
				triangle[row,i][1] = triangle[row-1,i-1][1] + triangle[row,i][0] if triangle[row-1,i-1][1] >= triangle[row-1,i][1] else triangle[row-1,i][1] + triangle[row,i][0]	

	return max([triangle[max_row-1,i][1] for i in xrange(max_row)])
		
if __name__ == "__main__":
	print run(parse_args(sys.argv[1:]))