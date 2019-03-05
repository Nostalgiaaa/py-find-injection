import mock

DAO = mock.Mock()

query = 1 + 2
query = "SELECT foo FROM bar WHERE id="
query = query + "2"
cursor = DAO.where(query)
