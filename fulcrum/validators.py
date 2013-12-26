class BaseValidator(object):
    def __init__(self, obj):
        self.data = obj
        self.errors = {}
        self.validate()

    def add_error(self, key, data_name, error):
        if key in self.errors:
            if data_name in self.errors[key]:
                self.errors[key][data_name].append(error)
            else:
                self.errors[key][data_name] = [error]
        else:
            self.errors[key] = {}
            self.errors[key][data_name] = [error]

    @property
    def valid(self):
        return len(self.errors) == 0

    def __repr__(self):
        if len(self.errors):
            printable_errors = []
            for key in self.errors:
                if isinstance(self.errors[key], list):
                    for error in self.errors[key]:
                        error_sentence = '{0} {1}.'.format(key, error)
                else:
                    for data_name in self.errors[key]:
                        for error in self.errors[key][data_name]:
                            error_sentence = '{0} {1} {2}.'.format(key, data_name, error)
                printable_errors.append(error_sentence)
            return ' '.join(printable_errors)



class FormValidator(BaseValidator):
    def validate(self):
        if not 'form' in self.data:
            self.errors.setdefault('form', []).append('must exist and not be empty')
        else:
            form = self.data['form']

            if 'name' not in form or ('name' in form and not len(form['name'])):
                self.add_error('form', 'name', 'must exist and not be empty')
            if 'elements' not in form or ('elements' in form and isinstance(form['elements'], list) and not len(form['elements'])):
                self.add_error('form', 'elements', 'must exist and not be empty')


class RecordValidator(BaseValidator):
    required_members = {
        'latitude': (int, float),
        'longitude': (int, float),
        'form_id': str,
        'form_values': dict
    }

    def _type_or_types_to_str(self, type_or_types):
        def repr_to_str(repr):
            return repr.split(" '")[1].split("'>")[0]
        if isinstance(type_or_types, (list, tuple)):
            types = []
            for repr in type_or_types:
                types.append(repr_to_str(str(repr)))
            return ' or '.join(types)
        else:
            return repr_to_str(str(type_or_types))

    def validate(self):
        if not 'record' in self.data:
            self.errors.setdefault('record', []).append('must exist and not be empty')
        else:
            record = self.data['record']

            for required_member, type_or_types in self.required_members.iteritems():
                if required_member not in record or (required_member in record and not isinstance(record[required_member], type_or_types)):
                    self.add_error('record', required_member, 'must exist and be of type {0}'.format(self._type_or_types_to_str(type_or_types)))

            if 'form_values' in record and record['form_values'] == {}:
                self.add_error('record', 'form_values', 'must exist and be of type dict and not be empty')