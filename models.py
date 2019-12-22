from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import text

from access_mgmt.app import db


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    dt_created = Column(DateTime(timezone=True), server_default=text('now()'))
    username = Column(Text, unique=True, nullable=False)

    def __init__(
            self,
            username: str
    ):
        self.username = username

    def __repr__(self):
        return f'<User(username={self.username})>'


class ServiceResource(db.Model):
    __tablename__ = 'service_resource'

    id = Column(Integer, primary_key=True)
    dt_created = Column(DateTime(timezone=True), server_default=text('now()'))
    service = Column(Text, unique=False, nullable=False)
    resource = Column(Text, unique=False, nullable=False)

    def __repr__(self):
        return f'<ServiceResource(id={self.id}, service={self.service}, ' \
               f'resource={self.resource})>'


class Permission(db.Model):
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True)
    dt_created = Column(DateTime(timezone=True), server_default=text('now()'))
    name = Column(Text, unique=True, nullable=False)
    description = Column(Text, unique=False, nullable=False)
    service_resource_id = Column(Integer, ForeignKey(ServiceResource.id))

    def __init__(
            self,
            name: str
    ):
        self.name = name

    def __repr__(self):
        return f'<Permission(name={self.name})>'


class Role(db.Model):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    dt_created = Column(DateTime(timezone=True), server_default=text('now()'))
    name = Column(Text, unique=True, nullable=False)
    description = Column(Text, unique=False, nullable=False)

    def __init__(
            self,
            name: str
    ):
        self.name = name

    def __repr__(self):
        return f'<Role(name={self.name})>'


class RolePermission(db.Model):
    __tablename__ = 'role_permission'

    id = Column(Integer, primary_key=True)
    dt_created = Column(DateTime(timezone=True), server_default=text('now()'))
    permission_id = Column(Integer, ForeignKey(Permission.id))
    role_id = Column(Integer, ForeignKey(Role.id))

    def __init__(
            self,
            name: str
    ):
        self.name = name

    def __repr__(self):
        return f'<RolePermission(permission_id={self.permission_id}, ' \
               f'role_id={self.role_id})>'


class UserRole(db.Model):
    __tablename__ = 'user_role'

    id = Column(Integer, primary_key=True)
    dt_created = Column(DateTime(timezone=True), server_default=text('now()'))
    user_id = Column(Integer, ForeignKey(User.id))
    role_id = Column(Integer, ForeignKey(Role.id))

    def __init__(
            self,
            name: str
    ):
        self.name = name

    def __repr__(self):
        return f'<UserRole(user_id={self.user_id}, role_id={self.role_id})>'


class UserPermission(db.Model):
    __tablename__ = 'user_permission'

    id = Column(Integer, primary_key=True)
    dt_created = Column(DateTime(timezone=True), server_default=text('now()'))
    user_id = Column(Integer, ForeignKey(User.id))
    permission_id = Column(Integer, ForeignKey(Permission.id))

    def __init__(
            self,
            name: str
    ):
        self.name = name

    def __repr__(self):
        return f'<UserPermission(user_id={self.user_id}, ' \
               f'permission_id={self.permission_id})>'
