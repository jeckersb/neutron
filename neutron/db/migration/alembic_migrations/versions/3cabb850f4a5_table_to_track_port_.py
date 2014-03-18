# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2013 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""Table to track port to host associations

Revision ID: 3cabb850f4a5
Revises: 5918cbddab04
Create Date: 2013-06-24 14:30:33.533562

"""

# revision identifiers, used by Alembic.
revision = '3cabb850f4a5'
down_revision = '5918cbddab04'

# Change to ['*'] if this migration applies to all plugins

migration_for_plugins = [
    'neutron.plugins.bigswitch.plugin.NeutronRestProxyV2'
]

from alembic import op
import sqlalchemy as sa


from neutron.db import migration


def upgrade(active_plugins=None, options=None):
    if not migration.should_run(active_plugins, migration_for_plugins):
        return

    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portlocations',
                    sa.Column('port_id', sa.String(length=255),
                              primary_key=True, nullable=False),
                    sa.Column('host_id',
                              sa.String(length=255), nullable=False),
                    mysql_engine='InnoDB'
                    )
    ### end Alembic commands ###


def downgrade(active_plugins=None, options=None):
    if not migration.should_run(active_plugins, migration_for_plugins):
        return

    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portlocations')
    ### end Alembic commands ###
