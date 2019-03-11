import mock

DAO = mock.Mock()
uid = 1

DAO.raw_sql("SELECT foo FROM bar")
DAO.raw_sql("SELECT foo FROM bar WHERE id=%s", uid)


DAO.raw_sql("SELECT * from {0} where id=%s".format(DAO.Meta.table), uid)
DAO.raw_sql("SELECT * from {table} where id=%s".format(table=DAO.Meta.table), uid)
DAO.raw_sql("{table1} join {table2}".format(DAO.Meta.table, DAO.Meta.table))
sql = "SELECT foo from {0} WHERE id=%s".format("bar")  # noqa
DAO.raw_sql(sql)
DAO.raw_sql("SELECT * from %s where id=%s" % ("test", 1))

unused_str = "{0}".format(1)
