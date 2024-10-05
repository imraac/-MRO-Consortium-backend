

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import validates
# import re
# from datetime import datetime

# db = SQLAlchemy()

# class User(db.Model):
#     __tablename__ = 'users'  
#     actions = db.relationship('UserAction', back_populates='user', cascade='all, delete-orphan')

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(129), nullable=False)
#     role = db.Column(db.String(50), default='user')
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Use datetime.utcnow
#     agency_id = db.Column(db.Integer, db.ForeignKey('agencies.id'), nullable=True)  

#     # Define a relationship to the Agency
#     agency = db.relationship('Agency', back_populates='users', foreign_keys=[agency_id])

#     # Other relationships
#     contact_details = db.relationship('ContactDetail', back_populates='user', cascade='all, delete-orphan')
#     founders = db.relationship('Founder', back_populates='user', cascade='all, delete-orphan')
#     board_directors = db.relationship('BoardDirector', back_populates='user', cascade='all, delete-orphan')
#     key_staff = db.relationship('KeyStaff', back_populates='user', cascade='all, delete-orphan')
#     consortiums = db.relationship('Consortium', back_populates='user', cascade='all, delete-orphan')
#     member_accounts = db.relationship('MemberAccountAdministrator', back_populates='user', cascade='all, delete-orphan')

#     @validates('email')
#     def validate_email(self, key, email):
#         regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
#         if not re.match(regex, email):
#             raise ValueError("Invalid email address")
#         return email

#     def __repr__(self):
#         return f"<User {self.id}: {self.username}>"

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "username": self.username,
#             "email": self.email,
#             "role": self.role,
#             "created_at": self.created_at.isoformat(),  # Convert to ISO format
#             "agency_id": self.agency_id  
#         }
    
#     class UserAction(db.Model):
#      __tablename__ = 'user_actions'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     action = db.Column(db.String(255), nullable=False)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)

#     user = db.relationship('User', back_populates='actions')

#     def __repr__(self):
#         return f"<UserAction {self.id}: {self.action} by User {self.user_id} at {self.timestamp}>"

#     def as_dict(self):
#         return {
#             'id': self.id,
#             'user_id': self.user_id,
#             'action': self.action,
#             'timestamp': self.timestamp.isoformat(),
#         }


# class Agency(db.Model):
#     __tablename__ = 'agencies'
    
#     id = db.Column(db.Integer, primary_key=True)
#     full_name = db.Column(db.String(150), nullable=False)
#     acronym = db.Column(db.String(50), nullable=True)
#     description = db.Column(db.Text, nullable=False)
#     mission_statement = db.Column(db.Text, nullable=False)
#     website = db.Column(db.String(255), nullable=False)
#     is_ngo = db.Column(db.Boolean, nullable=False)
#     years_operational = db.Column(db.Integer, nullable=False)
#     reason_for_joining = db.Column(db.Text, nullable=False)
#     willing_to_participate = db.Column(db.Boolean, nullable=False)
#     commitment_to_principles = db.Column(db.Boolean, nullable=False)

#     users = db.relationship('User', back_populates='agency')  # Use 'users' to denote multiple User instances

#     def __repr__(self):
#         return f"<Agency {self.id}: {self.full_name}>"

#     def as_dict(self):
#         return {  # Define a method to convert the model instance to a dictionary if needed
#             'id': self.id,
#             'full_name': self.full_name,
#             'acronym': self.acronym,
#             'description': self.description,
#             'mission_statement': self.mission_statement,
#             'website': self.website,
#             'is_ngo': self.is_ngo,
#             'years_operational': self.years_operational,
#             'reason_for_joining': self.reason_for_joining,
#             'willing_to_participate': self.willing_to_participate,
#             'commitment_to_principles': self.commitment_to_principles,
#           # Include user_id if necessary
#         }
# # ContactDetail Model
# class ContactDetail(db.Model):
#     __tablename__ = 'contact_detail'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150), nullable=False)
#     contact = db.Column(db.String(100), nullable=False)
#     clan = db.Column(db.String(100), nullable=True)
#     role = db.Column(db.String(50), nullable=False)

#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     user = db.relationship('User', back_populates='contact_details')

#     def __repr__(self):
#         return f"<ContactDetail {self.id}: {self.name}>"

#     def as_dict(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'contact': self.contact,
#             'clan': self.clan,
#             'role': self.role
#         }

# # Founder Model
# class Founder(db.Model):
#     __tablename__ = 'founder'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     contact = db.Column(db.String(100), nullable=False)
#     clan = db.Column(db.String(100), nullable=False)

#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     user = db.relationship('User', back_populates='founders')

#     def __repr__(self):
#         return f"<Founder {self.id}: {self.name}>"

#     def as_dict(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'contact': self.contact,
#             'clan': self.clan
#         }

# # BoardDirector Model
# class BoardDirector(db.Model):
#     __tablename__ = 'board_director'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     contact = db.Column(db.String(100), nullable=False)
#     clan = db.Column(db.String(100), nullable=False)

#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     user = db.relationship('User', back_populates='board_directors')

#     def __repr__(self):
#         return f"<BoardDirector {self.id}: {self.name}>"

#     def as_dict(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'contact': self.contact,
#             'clan': self.clan
#         }

# # KeyStaff Model
# class KeyStaff(db.Model):
#     __tablename__ = 'key_staff'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     contact = db.Column(db.String(100), nullable=False)
#     clan = db.Column(db.String(100), nullable=False)

#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     user = db.relationship('User', back_populates='key_staff')

#     def __repr__(self):
#         return f"<KeyStaff {self.id}: {self.name}>"

#     def as_dict(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'contact': self.contact,
#             'clan': self.clan
#         }

# # Consortium Model
# class Consortium(db.Model):
#     __tablename__ = 'consortium'

#     id = db.Column(db.Integer, primary_key=True)
#     active_year = db.Column(db.String(4), nullable=False)
#     partner_ngos = db.Column(db.Text, nullable=False)
#     international_staff = db.Column(db.Integer, nullable=False)
#     national_staff = db.Column(db.Integer, nullable=False)
#     program_plans = db.Column(db.Text, nullable=False)
#     main_donors = db.Column(db.Text, nullable=False)
#     annual_budget = db.Column(db.String(20), nullable=False)
#     membership_type = db.Column(db.String(50), nullable=False)

#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     user = db.relationship('User', back_populates='consortiums')

#     def __repr__(self):
#         return f"<Consortium {self.id}: {self.active_year}>"

#     def as_dict(self):
#         return {
#             'id': self.id,
#             'active_year': self.active_year,
#             'user_id': self.user_id
#         }

# # MemberAccountAdministrator Model
# class MemberAccountAdministrator(db.Model):
#     __tablename__ = 'member_account_administrator'  
#     id = db.Column(db.Integer, primary_key=True)
#     agency_registration_date = db.Column(db.Date, nullable=False)
#     agency_registration_number = db.Column(db.String(100), nullable=False)
#     hq_name = db.Column(db.String(100), nullable=False)
#     hq_position = db.Column(db.String(100), nullable=False)
#     hq_email = db.Column(db.String(100), nullable=False)
#     hq_address = db.Column(db.String(200), nullable=False)
#     hq_city = db.Column(db.String(100), nullable=False)
#     hq_state = db.Column(db.String(100), nullable=False)
#     hq_country = db.Column(db.String(100), nullable=False)
#     hq_zip_code = db.Column(db.String(10), nullable=False)

#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     user = db.relationship('User', back_populates='member_accounts')

#     def __repr__(self):
#         return f"<MemberAccountAdministrator {self.id}: {self.hq_name}>"

#     def as_dict(self):
#         return {
#             'id': self.id,
#             'user_id': self.user_id,
#             'agency_registration_date': self.agency_registration_date.isoformat(),  # Convert to ISO format
#             'agency_registration_number': self.agency_registration_number,
#             'hq_name': self.hq_name,
#             'hq_position': self.hq_position,
#             'hq_email': self.hq_email,
#             'hq_address': self.hq_address,
#             'hq_city': self.hq_city,
#             'hq_state': self.hq_state,
#             'hq_country': self.hq_country,
#             'hq_zip_code': self.hq_zip_code
#         }


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
import re
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

# User model
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(129), nullable=False)
    role = db.Column(db.String(50), default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    agency_id = db.Column(db.Integer, db.ForeignKey('agencies.id'), nullable=True)

    # Relationships
    actions = db.relationship('UserAction', back_populates='user', cascade='all, delete-orphan')
    agency = db.relationship('Agency', back_populates='users', foreign_keys=[agency_id])
    
    # Other relationships
    contact_details = db.relationship('ContactDetail', back_populates='user', cascade='all, delete-orphan')
    founders = db.relationship('Founder', back_populates='user', cascade='all, delete-orphan')
    board_directors = db.relationship('BoardDirector', back_populates='user', cascade='all, delete-orphan')
    key_staff = db.relationship('KeyStaff', back_populates='user', cascade='all, delete-orphan')
    consortiums = db.relationship('Consortium', back_populates='user', cascade='all, delete-orphan')
    member_accounts = db.relationship('MemberAccountAdministrator', back_populates='user', cascade='all, delete-orphan')

    @validates('email')
    def validate_email(self, key, email):
        regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
        if not re.match(regex, email):
            raise ValueError("Invalid email address")
        return email

    def __repr__(self):
        return f"<User {self.id}: {self.username}>"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "created_at": self.created_at.isoformat(),
            "agency_id": self.agency_id  
        }

# UserAction model
class UserAction(db.Model):
    __tablename__ = 'user_actions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    action = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='actions')

    def __repr__(self):
        return f"<UserAction {self.id}: {self.action} by User {self.user_id} at {self.timestamp}>"

    def as_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'action': self.action,
            'timestamp': self.timestamp.isoformat(),
        }

# Agency model
class Agency(db.Model):
    __tablename__ = 'agencies'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    acronym = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=False)
    mission_statement = db.Column(db.Text, nullable=False)
    website = db.Column(db.String(255), nullable=False)
    is_ngo = db.Column(db.Boolean, nullable=False)
    years_operational = db.Column(db.Integer, nullable=False)
    reason_for_joining = db.Column(db.Text, nullable=False)
    willing_to_participate = db.Column(db.Boolean, nullable=False)
    commitment_to_principles = db.Column(db.Boolean, nullable=False)

    # Relationship to users
    users = db.relationship('User', back_populates='agency')  # Use 'users' to denote multiple User instances

    def __repr__(self):
        return f"<Agency {self.id}: {self.full_name}>"

    def as_dict(self):
        return {  
            'id': self.id,
            'full_name': self.full_name,
            'acronym': self.acronym,
            'description': self.description,
            'mission_statement': self.mission_statement,
            'website': self.website,
            'is_ngo': self.is_ngo,
            'years_operational': self.years_operational,
            'reason_for_joining': self.reason_for_joining,
            'willing_to_participate': self.willing_to_participate,
            'commitment_to_principles': self.commitment_to_principles,
        }


class ContactDetail(db.Model):
    __tablename__ = 'contact_detail'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    clan = db.Column(db.String(100), nullable=True)
    role = db.Column(db.String(50), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='contact_details')

    def __repr__(self):
        return f"<ContactDetail {self.id}: {self.name}>"

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact': self.contact,
            'clan': self.clan,
            'role': self.role
        }


class Founder(db.Model):
    __tablename__ = 'founder'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    clan = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='founders')

    def __repr__(self):
        return f"<Founder {self.id}: {self.name}>"

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact': self.contact,
            'clan': self.clan
        }

class BoardDirector(db.Model):
    __tablename__ = 'board_director'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    clan = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='board_directors')

    def __repr__(self):
        return f"<BoardDirector {self.id}: {self.name}>"

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact': self.contact,
            'clan': self.clan
        }


class KeyStaff(db.Model):
    __tablename__ = 'key_staff'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    clan = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='key_staff')

    def __repr__(self):
        return f"<KeyStaff {self.id}: {self.name}>"

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact': self.contact,
            'clan': self.clan
        }


class Consortium(db.Model):
    __tablename__ = 'consortium'

    id = db.Column(db.Integer, primary_key=True)
    active_year = db.Column(db.String(4), nullable=False)
    partner_ngos = db.Column(db.Text, nullable=False)
    international_staff = db.Column(db.Integer, nullable=False)
    national_staff = db.Column(db.Integer, nullable=False)
    program_plans = db.Column(db.Text, nullable=False)
    main_donors = db.Column(db.Text, nullable=False)
    annual_budget = db.Column(db.String(20), nullable=False)
    membership_type = db.Column(db.String(50), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='consortiums')

    def __repr__(self):
        return f"<Consortium {self.id}: {self.active_year}>"

    def as_dict(self):
        return {
            'id': self.id,
            'active_year': self.active_year,
            'partner_ngos': self.partner_ngos,
            'international_staff': self.international_staff,
            'national_staff': self.national_staff,
            'program_plans': self.program_plans,
            'main_donors': self.main_donors,
            'annual_budget': self.annual_budget,
            'membership_type': self.membership_type
        }


class MemberAccountAdministrator(db.Model):
    __tablename__ = 'member_account_administrator'

    id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(100), nullable=False)
    member_email = db.Column(db.String(100), nullable=False)

  
    agency_registration_date = db.Column(db.Date, nullable=False)
    agency_registration_number = db.Column(db.String(100), nullable=False)
    hq_name = db.Column(db.String(100), nullable=False)
    hq_position = db.Column(db.String(100), nullable=False)
    hq_email = db.Column(db.String(100), nullable=False)
    hq_address = db.Column(db.String(200), nullable=False)
    hq_city = db.Column(db.String(100), nullable=False)
    hq_state = db.Column(db.String(100), nullable=False)
    hq_country = db.Column(db.String(100), nullable=False)
    hq_zip_code = db.Column(db.String(10), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='member_accounts')

    def __repr__(self):
        return f"<MemberAccountAdministrator {self.id}: {self.hq_name}>"

    def as_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'member_name': self.member_name,
            'member_email': self.member_email,
            'agency_registration_date': self.agency_registration_date.isoformat(),  
            'agency_registration_number': self.agency_registration_number,
            'hq_name': self.hq_name,
            'hq_position': self.hq_position,
            'hq_email': self.hq_email,
            'hq_address': self.hq_address,
            'hq_city': self.hq_city,
            'hq_state': self.hq_state,
            'hq_country': self.hq_country,
            'hq_zip_code': self.hq_zip_code
        }
