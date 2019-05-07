"""
Author: Andrea Murphy and Mohamed Ali Metwally
Date: April 16, 2019
DESC: Application of a dynamoDB Graph Database
"""

from py2neo import Graph, Node, Relationship

g = Graph(password="")

tx = g.begin()
rfc = Node("rfc_1918", name="Address Allocation for Private Internets")
tx.create(rfc)

links = Node("Links", name="Docs", address="https://tools.ietf.org/html/")
tx.create(links)

rfc_edge = Relationship(rfc, "Linked To", links)
tx.create(rfc_edge)

tx.commit()


