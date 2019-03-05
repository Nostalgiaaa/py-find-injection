import mock

DAO = mock.Mock()


DAO.raw_sql("SELECT foo from bar WHERE id=%s" % 2)

DAO.raw_sql("SELECT foo FROM bar where id={0}".format(1))

DAO.raw_sql("SELECT foo FROM bar where id={id}".format(id=1))