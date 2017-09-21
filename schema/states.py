# JCM added

from util import findWithNa
from util import getNodeOrNone
from util import findTrueFalse
from base import Base
from filing import Filing
import sqlalchemy as db
import sqlalchemy.dialects.mysql as m
from sqlalchemy.orm import relationship

def states(lookup, filing):
    ret = []

    allStates = lookup.findMultiWithNa("states", "StatesWhereCopyOfReturnIsFldCd")
    if allStates:
        for state in allStates:
            e = States()
            e.filing = filing
            e.State =  state.text
            ret.append(e)
    return ret

class States(Base):
    __tablename__ = "states"
    id = db.Column(db.Integer, primary_key=True)
    FilingId = db.Column(db.Integer, db.ForeignKey('filing.id'))
    State = db.Column(db.String(255))


    filing = relationship(Filing)
