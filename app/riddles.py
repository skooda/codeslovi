riddles = [
    {
        'text': 'Kolik jazyků znáš, tolikrát jsi člověkem',
        'answers': ['kolik jazyku znas, tolikrat jsi clovekem', 'kolik reci znas, tolikrat jsi clovekem', 'kolika recmi hovoris, tolikrat jsi clovekem'],
        'code': '''
$handle = fopen("php://stdin","r");
$languageKnowledge = (int)fgets($handle);
$humanity = 1;
$humanityMultiplier = 1;

for ($i = 0, $i >= $languageKnowledge; $i++) {
   $humanity *= $humanityMultiplier;
}

echo $humanity;
'''},

    # ------------------------------------------------------------------------------------------------------------------
    {
        'text': 'Jak se do lesa volá, tak se z lesa ozývá',
        'answers': ['jak se do lesa vola, tak se z lesa ozyva', 'jak se do lesa hulaka, tak se z lesa ozyva'],
        'code': '''
class Forest {
    function __construct($treeCount) {
      $this->treeCount = $treeCount;
    }

    function call(message) {
      return message;
    }
}
'''},

    # ------------------------------------------------------------------------------------------------------------------
    {
        'text': 'Bez peněz do hospody nelez',
        'answers': ['bez penez do hospody nelez', 'bez penez do krcmy nelez', 'bez penez do hospody nechod'],
        'code': '''
class Life
{

    /** @var float */
    private $money;

    /** @var bool */
    private $inPub = false;

    /**
     * @param float $money
     */
    public function __construct(float $money)
    {
        $this->money = $money;
    }

    public function goToPub()
    {
        if ($this->money <= 0) {
            throw new \RuntimeException('Not enough money.');
        }

        $this->inPub = true;
    }

}
'''},

    # ------------------------------------------------------------------------------------------------------------------
    {
        'text': 'Tak dlouho se chodí se džbánem pro vodu, až se ucho utrhne',
        'answers': ['tak dlouho se chodi se dzbanem pro vodu, az se ucho utrhne', 'tak dlouho se chodi s hrncem pro vodu, az se ucho utrhne'],
        'code': '''class Carafe {

    public function __construct($stamina = 1000) {
        $this->stamina = $stamina;
        $this->content = Null;
    }

    public function goToWell() {
        $this->position = 'well';
        $this->content = 'water';
        $this->stamina--;

        if ($stamina <= 0) {
           throw new CarafeBrokenException('Handle broken')
        }
    }

    public function goHome() {
        $this->position = 'home';
        $this->content = Null;
    }
}

$carafe = new Carafe();
while (True) {
    $carafe->goToWell();
    $carafe->goHome();
}
'''},

    # ------------------------------------------------------------------------------------------------------------------
    {
        'text': 'Chybami se člověk učí',
        'answers': ['chybami se clovek uci', 'chybama se ucime'],
        'code': '''
$life = new Life();
$experience = 0;
while (isAlive()) {
    try {
        $step = $life->getNextStep();
        $step->execute();
    } catch (\Exception $e) {
        $experience++;
    }
}'''}
]
