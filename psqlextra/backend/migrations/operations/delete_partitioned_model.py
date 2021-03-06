from django.db.migrations.operations.models import DeleteModel


class PostgresDeletePartitionedModel(DeleteModel):
    """Deletes the specified partitioned model."""

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        """Apply this migration operation forwards."""

        model = from_state.apps.get_model(app_label, self.name)
        if self.allow_migrate_model(schema_editor.connection.alias, model):
            schema_editor.delete_partitioned_model(model)

    def database_backwards(
        self, app_label, schema_editor, from_state, to_state
    ):
        """Apply this migration operation backwards."""

        model = to_state.apps.get_model(app_label, self.name)
        if self.allow_migrate_model(schema_editor.connection.alias, model):
            schema_editor.create_partitioned_model(model)

    def describe(self):
        """Gets a human readable text describing this migration."""

        description = super().describe()
        description = description.replace("model", "partitioned model")
        return description
