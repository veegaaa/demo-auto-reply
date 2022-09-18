"""empty message

Revision ID: 88e0f36b9721
Revises: 7a904b5361a3
Create Date: 2020-05-31 22:46:58.480937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88e0f36b9721'
down_revision = '7a904b5361a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('applications', sa.Column('name', sa.String(length=50), nullable=False))
    op.drop_column('applications', 'student_name')
    op.alter_column('bookings', 'student_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookings', 'student_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.add_column('applications', sa.Column('student_name', sa.VARCHAR(length=50), nullable=False))
    op.drop_column('applications', 'name')
    # ### end Alembic commands ###
