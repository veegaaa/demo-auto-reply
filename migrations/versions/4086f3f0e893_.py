"""empty message

Revision ID: 4086f3f0e893
Revises: 4fee434d949a
Create Date: 2020-05-31 23:01:54.867023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4086f3f0e893'
down_revision = '4fee434d949a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('applications', 'phone_number',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('applications', 'student_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('bookings', 'student_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookings', 'student_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('applications', 'student_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('applications', 'phone_number',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###
