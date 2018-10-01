#! /usr/bin/env python3

import os                   # to manage files in local directory path
from SPARQLWrapper import SPARQLWrapper, JSON #to sparql query the web
import rdflib               # to use rdflib
import rdfextras            # to use rdflib
import rdflib.graph as g    # to use rdflib
rdfextras.registerplugins() # so we can Graph.query()
import sys                  #to take in arguments
import fileinput            #to input files
import re                   #to filter files using regex
import unicodedata          #to convert literals to strings



##### Code section which merges the rdf files into a single datastore.ttl file #####

#remove a previously existing datastore.ttl as not to get any duplicates
if os.path.isfile('datastore.ttl') == True :
    os.remove('datastore.ttl')

# list all the files in the directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

#filter for .ttl files using regex search:
regex = re.compile('[.]ttl')
selected_files = filter(regex.search, files)

#use the rdflib module to parse all the .ttl files to make a single datastore triple file datastore.ttl.
graph = g.ConjunctiveGraph()
[graph.parse(str(s), format='ttl') for s in selected_files]

#output_datastore = graph.serialize(format='ttl')

graph.serialize(destination='datastore.ttl', format='turtle')


### parse a local knowledge graph rdf file in this case the datastore.ttl



########################################################################
# read in file which was given as the first commandline argument
# the file should be a list of PURLS
in_file = open(str(sys.argv[1]), 'r')

#Create and clean a list of PURLS from the inputfile
in_args = []
in_args += [line.rstrip('\n') for line in in_file]

########################################################################
# Put together a sparql query from pieces.

# Put together the PREFIX block:
def prefix_func():
    prefix_list = ['obo: <http://purl.obolibrary.org/obo/>', 'rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>', 'rdfs: <http://www.w3.org/2000/01/rdf-schema#>', 'owl: <http://www.w3.org/2002/07/owl#>', 'html: <http://tools.ietf.org/html/>']
    insert_prefix = ' \nPREFIX '
    return ('PREFIX ' + insert_prefix.join(prefix_list) + '\n' )

# Put together a select block
#takes the query and a bool for whether or not to add a distinct
def select_func():
    s = 'SELECT ?value ?x \n'
    return s

# Put together the FROM block
def from_func():
    return 'FROM <datastore.ttl>\n'

# Put together a VALUES block to filter using a single variable/column
def values_filtering_func(input_list, in_var):
    s = '>)\n(<'
    return 'VALUES (?'+ str(in_var) +') { \n(<' + s.join(input_list) + '>) \n}\n'


# Put together a WHERE clause which will only be used to query_associated_data
# using the values_filtering_func which takes in an input PURL list
def where_query_associated_data_func():
    s = 'WHERE {\n'
    s += '?value obo:ENVO_09200014 ?x'
    s += '} \n'
    s += values_filtering_func(in_args,'value') + '\n'
    #s += '} \n'
    return s


#Put together a sparql query which will retrieve data from the datastore which
#has columns annotated with any PURLs given as input
def query_associated_data():
    f_list = [prefix_func(), select_func() , from_func(), where_query_associated_data_func() ]
    return''.join(f_list)

#print query_associated_data()

#print prefix_func()
#print select_func()
#print from_func()
#print where_query_associated_data_func()

#print query_property_path_func('c','value')
#print values_filtering_func(in_args,'value')

#print(query_associated_data())


# initialize the ConjunctiveGraph which will function as the entire datastore
graph = g.ConjunctiveGraph()

graph.parse('datastore.ttl', format='ttl')

results = graph.query(query_associated_data())

for row in results:
    print("%s | %s" % row)

# subj = []
# pred = []
# obj = []
# for (s, p, o) in results:
#     subj.append((unicodedata.normalize('NFKD', s.toPython()).encode('ascii','ignore')).split(', '))
#     pred.append((unicodedata.normalize('NFKD', p.toPython()).encode('ascii','ignore')).split(', '))
#     obj.append((unicodedata.normalize('NFKD', o.toPython()).encode('ascii','ignore')).split(', '))
#
# #create output csv file
# outstring = 'test'
# f = open(outstring, 'w')
# for x in xrange(0,len(results)):
#     f.write( str( subj[x].pop() ) + ',' +  str(len(pred[x])) + ',' + str(len(obj[x])) + '\n' )
